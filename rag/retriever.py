"""
===========================================
FAISS Retriever
===========================================
Loads the FAISS vector database and retrieves
the most relevant documents using Max
Marginal Relevance (MMR).
MMR returns relevant AND diverse chunks,
reducing duplicate context.
"""
from pathlib import Path
from typing import List
from langchain_core.documents import Document
from langchain_community.vectorstores import FAISS
from rag.config import (
    VECTOR_DB_PATH,
    TOP_K,
    FETCH_K,
    MMR_LAMBDA,
)
from rag.embeddings import EmbeddingModel
class Retriever:
    _db = None
    @classmethod
    def load(cls):
        if cls._db is None:
            if not Path(VECTOR_DB_PATH).exists():
                raise FileNotFoundError(
                    "Vector database not found.\nRun build_index.py first."
                )
            print("=" * 50)
            print("Loading Vector Database...")
            print("=" * 50)
            embedding = EmbeddingModel.load()
            cls._db = FAISS.load_local(
                str(VECTOR_DB_PATH),
                embedding,
                allow_dangerous_deserialization=True,
            )
            print("Vector Database Loaded Successfully\n")
        return cls._db
    # ----------------------------------------
    # MMR Search (Recommended)
    # ----------------------------------------
    @classmethod
    def search(
        cls,
        query: str,
        k: int = TOP_K,
        fetch_k: int = FETCH_K,
        lambda_mult: float = MMR_LAMBDA,
    ) -> List[Document]:
        """
        Max Marginal Relevance retrieval.
        Parameters
        ----------
        query : str
            User question
        k : int
            Number of chunks returned
        fetch_k : int
            Number of candidate chunks to consider
        lambda_mult : float
            1.0 -> only relevance
            0.0 -> only diversity
            0.5 -> balanced
        """
        db = cls.load()
        return db.max_marginal_relevance_search(
            query=query,
            k=k,
            fetch_k=fetch_k,
            lambda_mult=lambda_mult,
        )
    # ----------------------------------------
    # Similarity Search (Optional)
    # ----------------------------------------
    @classmethod
    def similarity_search(
        cls,
        query: str,
        k: int = TOP_K,
    ):
        """
        Traditional cosine similarity search.
        Useful for comparison and debugging.
        """
        db = cls.load()
        return db.similarity_search(
            query=query,
            k=k,
        )
    # ----------------------------------------
    # Search with Scores
    # ----------------------------------------
    @classmethod
    def search_with_score(
        cls,
        query: str,
        k: int = TOP_K,
    ):
        db = cls.load()
        return db.similarity_search_with_score(
            query=query,
            k=k,
        )
    # ----------------------------------------
    # LangChain Retriever
    # ----------------------------------------
    @classmethod
    def as_retriever(
        cls,
        k: int = TOP_K,
        fetch_k: int = 20,
        lambda_mult: float = 0.5,
    ):
        db = cls.load()
        return db.as_retriever(
            search_type="mmr",
            search_kwargs={
                "k": k,
                "fetch_k": fetch_k,
                "lambda_mult": lambda_mult,
            },
        )
    # ----------------------------------------
    # Statistics
    # ----------------------------------------
    @classmethod
    def total_documents(cls):
        db = cls.load()
        return db.index.ntotal