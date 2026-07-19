from typing import List
from langchain_core.documents import Document
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    BaseMessage,
)
class PromptBuilder:
    DEFAULT_SYSTEM_PROMPT = """
    You are Shobhit's AI Portfolio Assistant.
    Rules:
    1. Answer greetings naturally.
    2. Use the provided context whenever possible.
    3. If the user asks about Shobhit, his projects, skills, education, or experience, answer only from the retrieved context.
    4. If the question is unrelated to the portfolio, politely say that you specialize in answering questions about Shobhit's portfolio.
    5. Never invent portfolio information.
    6. Be friendly and conversational.
    """
    @staticmethod
    def build_context(documents: List[Document]) -> str:
        context = []
        for i, doc in enumerate(documents, start=1):
            source = doc.metadata.get("filename", "Unknown")
            category = doc.metadata.get("category", "General")
            context.append(
                f"""
Document {i}
Category : {category}
Source   : {source}
Content:
{doc.page_content}
"""
            )
        return "\n".join(context)
    @classmethod
    def build_messages(
        cls,
        question: str,
        documents: List[Document],
        history: List[BaseMessage] = None,
        system_prompt: str = DEFAULT_SYSTEM_PROMPT,
    ):
        messages = []
        messages.append(
            SystemMessage(content=system_prompt)
        )
        if history:
            messages.extend(history)
        context = cls.build_context(documents)
        messages.append(
            HumanMessage(
                content=f"""
Context
=======
{context}
==============================
Question
{question}
"""
            )
        )
        return messages