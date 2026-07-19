from pathlib import Path
from langchain_core.documents import Document
from langchain_community.document_loaders import (
    TextLoader,
    PyPDFLoader,
    UnstructuredWordDocumentLoader,
    UnstructuredMarkdownLoader,
)
from rag.utils import build_source_metadata
from rag.logger import logger
SUPPORTED_EXTENSIONS = {
    ".txt",
    ".pdf",
    ".docx",
    ".md",
}
class DocumentLoader:
    @staticmethod
    def get_loader(filepath: str):
        ext = Path(filepath).suffix.lower()
        if ext == ".txt":
            return TextLoader(filepath, encoding="utf-8")
        elif ext == ".pdf":
            return PyPDFLoader(filepath)
        elif ext == ".docx":
            return UnstructuredWordDocumentLoader(filepath)
        elif ext == ".md":
            return UnstructuredMarkdownLoader(filepath)
        return None
    @classmethod
    def load_directory(cls, directory):
        documents = []
        directory = Path(directory)
        for file in directory.rglob("*"):
            if file.suffix.lower() not in SUPPORTED_EXTENSIONS:
                continue
            loader = cls.get_loader(str(file))
            if loader is None:
                continue
            try:
                docs = loader.load()
                metadata = build_source_metadata(str(file))
                for doc in docs:
                    doc.metadata.update(metadata)
                documents.extend(docs)
                logger.info(f"Loaded {file.name}")
            except Exception as e:
                logger.error(f"Failed loading {file.name}: {e}")
        logger.info(f"Total Documents: {len(documents)}")
        return documents