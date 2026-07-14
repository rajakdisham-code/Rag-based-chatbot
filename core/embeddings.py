"""
embeddings.py

Handles loading the embedding model and generating embeddings.
"""

from typing import List

import numpy as np
import streamlit as st
from sentence_transformers import SentenceTransformer

from core.config import EMBEDDING_MODEL
from core.logger import logger


@st.cache_resource
def load_embedding_model():
    """
    Load the embedding model only once.
    Streamlit will cache it across reruns.
    """

    logger.info("Loading embedding model...")

    model = SentenceTransformer(EMBEDDING_MODEL)

    logger.info("Embedding model loaded successfully.")

    return model


class EmbeddingModel:

    def __init__(self):
        self.model = load_embedding_model()

    def embed_documents(self, texts: List[str]) -> np.ndarray:

        return self.model.encode(
            texts,
            batch_size=32,
            show_progress_bar=False,
            convert_to_numpy=True,
            normalize_embeddings=True
        )

    def embed_query(self, query: str) -> np.ndarray:

        return self.model.encode(
            query,
            convert_to_numpy=True,
            normalize_embeddings=True
        )