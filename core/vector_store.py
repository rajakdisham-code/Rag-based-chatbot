"""
vector_store.py

Creates, saves, loads and searches a FAISS vector database.
"""

from pathlib import Path
import pickle

import faiss
import numpy as np

from core.logger import logger


class VectorStore:

    def __init__(self):

        self.index = None
        self.metadata = []

    def build(self, embeddings: np.ndarray, metadata: list):

        dimension = embeddings.shape[1]

        self.index = faiss.IndexFlatIP(dimension)

        self.index.add(embeddings.astype("float32"))

        self.metadata = metadata

        logger.info(f"FAISS Index Created with {len(metadata)} chunks.")

    def save(self, folder):

        folder = Path(folder)

        folder.mkdir(parents=True, exist_ok=True)

        faiss.write_index(
            self.index,
            str(folder / "index.faiss")
        )

        with open(folder / "metadata.pkl", "wb") as f:

            pickle.dump(self.metadata, f)

        logger.info("Vector Store Saved.")

    def load(self, folder):

        folder = Path(folder)

        self.index = faiss.read_index(
            str(folder / "index.faiss")
        )

        with open(folder / "metadata.pkl", "rb") as f:

            self.metadata = pickle.load(f)

        logger.info("Vector Store Loaded.")

    def search(self, query_embedding, top_k=5, min_score=0.60):

        scores, indices = self.index.search(
            np.array([query_embedding]).astype("float32"),
            top_k * 3  # retrieve extra results for filtering
        )

        results = []
        seen = set()

        for score, idx in zip(scores[0], indices[0]):

            if idx == -1:
                continue

            if score < min_score:
                continue

            chunk = self.metadata[idx]

            # Remove duplicate chunks
            key = (
                chunk["source"],
                chunk["page"],
                chunk["text"][:100]
            )

            if key in seen:
                continue

            seen.add(key)

            results.append({
                **chunk,
                "score": float(score)
            })

        results.sort(
            key=lambda x: x["score"],
            reverse=True
    )

        return results[:top_k]