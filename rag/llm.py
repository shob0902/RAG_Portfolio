"""
===========================================
LLM Manager
===========================================
Handles loading and interacting with the
chat model (Ollama).
Uses Singleton pattern so the model is
loaded only once.
"""
from typing import List, Union
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    SystemMessage,
    BaseMessage,
)
from langchain_ollama import ChatOllama
from rag.config import (
    OLLAMA_MODEL,
    OLLAMA_BASE_URL,
    TEMPERATURE,
    MAX_TOKENS,
)
class LLM:
    _instance = None
    @classmethod
    def load(cls):
        if cls._instance is None:
            print("=" * 50)
            print("Loading LLM...")
            print("=" * 50)
            cls._instance = ChatOllama(
                model=OLLAMA_MODEL,
                base_url=OLLAMA_BASE_URL,
                temperature=TEMPERATURE,
                num_predict=MAX_TOKENS,
            )
            print(f"Loaded Model : {OLLAMA_MODEL}\n")
        return cls._instance
    @classmethod
    def chat(cls, messages: List[BaseMessage]) -> AIMessage:
        """
        Send chat messages to the LLM.
        Parameters
        ----------
        messages : list[BaseMessage]
        Returns
        -------
        AIMessage
        """
        llm = cls.load()
        return llm.invoke(messages)
    @classmethod
    def generate(cls, prompt: str) -> str:
        """
        Convenience wrapper for a single
        user prompt.
        """
        response = cls.chat(
            [
                HumanMessage(content=prompt)
            ]
        )
        return response.content
    @classmethod
    def ask(
        cls,
        system_prompt: str,
        question: str,
    ) -> str:
        """
        Ask using a system prompt.
        Returns plain text.
        """
        messages = [
            SystemMessage(content=system_prompt),
            HumanMessage(content=question),
        ]
        response = cls.chat(messages)
        return response.content
    @classmethod
    def model_name(cls):
        return OLLAMA_MODEL