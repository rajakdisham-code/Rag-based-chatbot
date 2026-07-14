"""
retriever.py

Semantic retrieval using FAISS.
"""

from core.embeddings import EmbeddingModel
from core.vector_store import VectorStore
from core.config import VECTOR_STORE, TOP_K


class Retriever:

    def __init__(self):

        self.embedding_model = EmbeddingModel()

        self.vector_store = VectorStore()

        self.vector_store.load(VECTOR_STORE)

    def retrieve(self, query: str, top_k: int = TOP_K):

        query_embedding = self.embedding_model.embed_query(query)

        return self.vector_store.search(
            query_embedding=query_embedding,
            top_k=top_k,
            min_score=0.60
        )