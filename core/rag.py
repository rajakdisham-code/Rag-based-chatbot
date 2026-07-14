"""
rag.py

Main RAG pipeline.
Coordinates retrieval and answer generation.
"""

from core.retriever import Retriever
from core.generator import Generator
from core.logger import logger


class RAGPipeline:
    """
    Main RAG Pipeline.
    """

    def __init__(self):

        logger.info("Initializing RAG Pipeline...")

        self.retriever = Retriever()
        self.generator = Generator()

        logger.info("RAG Pipeline Ready.")

    def ask(self, query: str):

        # Retrieve relevant chunks
        retrieved_chunks = self.retriever.retrieve(query)

        # Generate answer
        answer = self.generator.generate(
            query=query,
            retrieved_chunks=retrieved_chunks,
        )

        return answer