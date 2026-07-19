import unittest
from unittest.mock import MagicMock, patch

from rag.retriever import Retriever


class RetrieverTests(unittest.TestCase):
    def test_ensure_index_builds_when_vector_db_missing(self):
        with patch("rag.retriever.Path.exists", return_value=False), \
             patch("rag.retriever.validate_dataset"), \
             patch("rag.retriever.DocumentLoader") as loader_cls, \
             patch("rag.retriever.DocumentSplitter") as splitter_cls, \
             patch("rag.retriever.Indexer") as indexer_cls:
            loader_cls.return_value.load_directory.return_value = [MagicMock()]
            splitter_cls.return_value.split.return_value = [MagicMock()]
            indexer_cls.return_value.create.return_value = MagicMock()

            Retriever.ensure_index()

        indexer_cls.return_value.create.assert_called_once()


if __name__ == "__main__":
    unittest.main()
