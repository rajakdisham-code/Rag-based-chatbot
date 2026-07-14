"""
ingest.py

Builds the FAISS index from all PDFs in the data folder.
"""

from core.logger import logger
from core.pdf_loader import load_pdfs
from core.chunker import create_chunks
from core.embeddings import EmbeddingModel
from core.vector_store import VectorStore
from core.config import VECTOR_STORE


def main():

    logger.info("Starting document ingestion...")

    documents = load_pdfs()

    chunks = create_chunks(documents)

    texts = [chunk["text"] for chunk in chunks]

    embedding_model = EmbeddingModel()

    embeddings = embedding_model.embed_documents(texts)

    vector_store = VectorStore()

    vector_store.build(
        embeddings=embeddings,
        metadata=chunks,
    )

    vector_store.save(VECTOR_STORE)

    logger.info("Ingestion completed successfully.")

    print()
    print("=" * 60)
    print("Documents :", len(documents))
    print("Chunks    :", len(chunks))
    print("Status    : Index Created Successfully")
    print("=" * 60)


if __name__ == "__main__":
    main()