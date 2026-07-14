"""
embeddings.py

Handles loading the embedding model and generating embeddings.
"""

from typing import List

import numpy as np
from sentence_transformers import SentenceTransformer

from core.config import EMBEDDING_MODEL
from core.logger import logger


class EmbeddingModel:
    """
    Singleton embedding model.

    Loads the model only once during application startup.
    """

    _instance = None

    def __new__(cls):
        if cls._instance is None:
            logger.info("Loading embedding model...")

            cls._instance = super().__new__(cls)

            cls._instance.model = SentenceTransformer(
                EMBEDDING_MODEL
            )

            logger.info("Embedding model loaded successfully.")

        return cls._instance

    def embed_documents(self, texts: List[str]) -> np.ndarray:
        """
        Generate embeddings for document chunks.
        """

        return self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=True,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_query(self, query: str) -> np.ndarray:
        """
        Generate embedding for a user query.
        """

        return self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )