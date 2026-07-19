from collections import deque
from typing import List
from langchain_core.messages import (
    AIMessage,
    HumanMessage,
    BaseMessage,
)
from rag.config import MAX_HISTORY
class ConversationMemory:
    def __init__(self, max_history=MAX_HISTORY):
        self.history = deque(maxlen=max_history * 2)
    def add_user_message(self, message: str):
        self.history.append(
            HumanMessage(content=message)
        )
    def add_ai_message(self, message: str):
        self.history.append(
            AIMessage(content=message)
        )
    def add_message(self, message: BaseMessage):
        self.history.append(message)
    def get_history(self) -> List[BaseMessage]:
        return list(self.history)
    def clear(self):
        self.history.clear()
    def size(self):
        return len(self.history)