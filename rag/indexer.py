from pathlib import Path
from langchain_community.vectorstores import FAISS
from rag.config import VECTOR_DB_PATH
from rag.embeddings import EmbeddingModel
from rag.logger import logger
class Indexer:
    def __init__(self):
        self.embedding = EmbeddingModel.load()
    def create(self, chunks):
        logger.info("Generating embeddings...")
        vector_db = FAISS.from_documents(
            documents=chunks,
            embedding=self.embedding
        )
        Path(VECTOR_DB_PATH).mkdir(
            parents=True,
            exist_ok=True
        )
        vector_db.save_local(
            str(VECTOR_DB_PATH)
        )
        logger.info(f"Vector database saved at {VECTOR_DB_PATH}")
        return vector_db
    @staticmethod
    def load():
        embedding = EmbeddingModel.load()
        return FAISS.load_local(
            str(VECTOR_DB_PATH),
            embedding,
            allow_dangerous_deserialization=True
        )