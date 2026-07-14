"""
PDF Loader Module

Loads all PDFs from the data folder and extracts text page by page.
"""

from pathlib import Path
import fitz  # PyMuPDF

from core.config import DATA_FOLDER
from core.logger import logger


def load_pdfs(data_folder: Path = DATA_FOLDER) -> list[dict]:
    """
    Returns:
        [
            {
                "text": "...",
                "source": "book.pdf",
                "page": 1
            }
        ]
    """

    documents = []

    if not data_folder.exists():
        raise FileNotFoundError(f"Data folder not found: {data_folder}")

    pdf_files = sorted(data_folder.glob("*.pdf"))

    if not pdf_files:
        raise FileNotFoundError("No PDF files found inside data folder.")

    logger.info(f"Found {len(pdf_files)} PDF(s).")

    for pdf in pdf_files:

        logger.info(f"Reading {pdf.name}")

        try:
            doc = fitz.open(pdf)

            for page_number, page in enumerate(doc, start=1):

                text = page.get_text("text").strip()

                if not text:
                    continue

                documents.append(
                    {
                        "text": text,
                        "source": pdf.name,
                        "page": page_number,
                    }
                )

            doc.close()

        except Exception as e:
            logger.error(f"Failed to read {pdf.name}: {e}")

    logger.info(f"Loaded {len(documents)} pages.")

    return documents