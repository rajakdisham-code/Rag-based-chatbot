"""
chunker.py

Splits PDF pages into overlapping chunks for embedding.
"""

from typing import List

from core.config import CHUNK_SIZE, CHUNK_OVERLAP
from core.logger import logger


def chunk_text(text: str,
               chunk_size: int = CHUNK_SIZE,
               overlap: int = CHUNK_OVERLAP) -> List[str]:
    """
    Split text into overlapping chunks.

    Returns:
        List[str]
    """

    chunks = []

    start = 0

    while start < len(text):

        end = min(start + chunk_size, len(text))

        chunk = text[start:end].strip()

        if chunk:
            chunks.append(chunk)

        if end == len(text):
            break

        start = end - overlap

    return chunks


def create_chunks(documents: list) -> list:
    """
    Converts page-wise documents into chunk-wise documents.

    Returns:
    [
        {
            "text": "...",
            "source": "...",
            "page": 5
        }
    ]
    """

    final_chunks = []

    for doc in documents:

        text_chunks = chunk_text(doc["text"])

        for chunk in text_chunks:

            final_chunks.append(
                {
                    "text": chunk,
                    "source": doc["source"],
                    "page": doc["page"]
                }
            )

    logger.info(f"Created {len(final_chunks)} chunks.")

    return final_chunks