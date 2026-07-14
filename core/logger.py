"""
logger.py

Central logging configuration for the RAG Chatbot.
"""

import logging
from logging.handlers import RotatingFileHandler
from pathlib import Path

from core.config import LOG_FOLDER

LOG_FILE = Path(LOG_FOLDER) / "chatbot.log"


def setup_logger(name: str = "RAGChatbot") -> logging.Logger:
    """
    Creates and returns a configured logger.

    Parameters
    ----------
    name : str
        Logger name.

    Returns
    -------
    logging.Logger
    """

    logger = logging.getLogger(name)

    if logger.handlers:
        return logger

    logger.setLevel(logging.INFO)

    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(filename)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    file_handler = RotatingFileHandler(
        LOG_FILE,
        maxBytes=5 * 1024 * 1024,
        backupCount=5,
        encoding="utf-8",
    )

    file_handler.setFormatter(formatter)

    console_handler = logging.StreamHandler()

    console_handler.setFormatter(formatter)

    logger.addHandler(file_handler)

    logger.addHandler(console_handler)

    logger.propagate = False

    return logger


logger = setup_logger()
