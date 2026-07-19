"""
===========================================
Logger Configuration
===========================================
Provides a centralized logger for the
entire Portfolio AI project.
"""
import logging
import sys
from rag.config import LOG_LEVEL
class Logger:
    _logger = None
    @classmethod
    def get_logger(cls):
        if cls._logger is not None:
            return cls._logger
        logger = logging.getLogger("PortfolioAI")
        logger.setLevel(LOG_LEVEL)
        logger.handlers.clear()
        console = logging.StreamHandler(sys.stdout)
        formatter = logging.Formatter(
            fmt="%(asctime)s | %(levelname)-8s | %(message)s",
            datefmt="%H:%M:%S"
        )
        console.setFormatter(formatter)
        logger.addHandler(console)
        logger.propagate = False
        cls._logger = logger
        return logger
logger = Logger.get_logger()