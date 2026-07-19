"""
====================================================
Build Vector Database
====================================================
Run:
python build_index.py
"""
import time
from rag.config import DATA_PATH
from rag.logger import logger
from rag.utils import validate_dataset
from rag.loaders import DocumentLoader
from rag.splitter import DocumentSplitter
from rag.indexer import Indexer
class BuildPipeline:
    def __init__(self):
        self.loader = DocumentLoader()
        self.splitter = DocumentSplitter()
        self.indexer = Indexer()
    def run(self):
        start = time.time()
        logger.info("=" * 60)
        logger.info("Starting Index Build")
        logger.info("=" * 60)
        validate_dataset(DATA_PATH)
        documents = self.loader.load_directory(DATA_PATH)
        if not documents:
            logger.error("No documents found.")
            return
        chunks = self.splitter.split(documents)
        self.indexer.create(chunks)
        end = time.time()
        logger.info("=" * 60)
        logger.info("Index Build Completed")
        logger.info(f"Documents : {len(documents)}")
        logger.info(f"Chunks    : {len(chunks)}")
        logger.info(f"Time      : {end-start:.2f} sec")
        logger.info("=" * 60)
if __name__ == "__main__":
    BuildPipeline().run()