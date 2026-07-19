"""
===========================================
Embedding Model Loader
===========================================
This module is responsible for loading the
embedding model only once during the lifetime
of the application.
Using a singleton pattern avoids loading the
same model multiple times, which saves RAM
and improves performance.
"""
from langchain_huggingface import HuggingFaceEmbeddings
from rag.config import EMBEDDING_MODEL


class EmbeddingModel:
    """
    Singleton wrapper around
    HuggingFaceEmbeddings.
    Example
    -------
    embedding = EmbeddingModel.load()
    """
    _instance = None
    @classmethod
    def load(cls):
        """
        Loads the embedding model.
        Returns
        -------
        HuggingFaceEmbeddings
        """
        if cls._instance is None:
            print("=" * 50)
            print("Loading Embedding Model...")
            print("=" * 50)
            try:
                cls._instance = HuggingFaceEmbeddings(
                    model_name=EMBEDDING_MODEL,
                    model_kwargs={
                        "device": "cpu"
                    },
                    encode_kwargs={
                        "normalize_embeddings": True
                    }
                )
            except Exception as exc:
                print(f"Embedding model load failed: {exc}")
                raise
            print("Embedding Model Loaded Successfully\n")
        return cls._instance
    @classmethod
    def model_name(cls):
        return EMBEDDING_MODEL
    @classmethod
    def dimension(cls):
        """
        MiniLM produces
        384-dimensional vectors.
        """
        return 384