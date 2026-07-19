from rag.retriever import Retriever
from rag.prompt_builder import PromptBuilder
from rag.memory import ConversationMemory
from rag.llm import LLM
class RAGChain:
    def __init__(self):
        self.memory = ConversationMemory()
    def ask(
        self,
        question: str,
        system_prompt: str = None,
    ):
        # Retrieve relevant documents
        documents = Retriever.search(question)
        # Build prompt
        messages = PromptBuilder.build_messages(
            question=question,
            documents=documents,
            history=self.memory.get_history(),
            system_prompt=system_prompt
            or PromptBuilder.DEFAULT_SYSTEM_PROMPT,
        )
        # Generate response
        response = LLM.chat(messages)
        # Update memory
        self.memory.add_user_message(question)
        self.memory.add_ai_message(response.content)
        # Return response with sources
        return {
            "answer": response.content,
            "sources": [
                {
                    "title": doc.metadata.get("title"),
                    "category": doc.metadata.get("category")
                }
                for doc in documents
            ],
        }
    def clear_memory(self):
        self.memory.clear()
    def history(self):
        return self.memory.get_history()