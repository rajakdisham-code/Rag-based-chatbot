"""
config.py

Centralized configuration for the RAG Chatbot.
Loads environment variables and exposes them throughout the project.
"""

from pathlib import Path
import os
from dotenv import load_dotenv

# ------------------------------------------------------------
# Load Environment Variables
# ------------------------------------------------------------

load_dotenv()

# ------------------------------------------------------------
# Base Directory
# ------------------------------------------------------------

BASE_DIR = Path(__file__).resolve().parent.parent

# ------------------------------------------------------------
# API Configuration
# ------------------------------------------------------------

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    raise ValueError(
        "❌ GEMINI_API_KEY not found.\n"
        "Please create a .env file and add your API key."
    )

# ------------------------------------------------------------
# Model Configuration
# ------------------------------------------------------------

GENERATION_MODEL = os.getenv(
    "MODEL_NAME",
    "gemini-3.5-flash"
)

EMBEDDING_MODEL = "BAAI/bge-base-en-v1.5"

# ------------------------------------------------------------
# Directory Configuration
# ------------------------------------------------------------

DATA_FOLDER = Path(
    os.getenv("DATA_FOLDER", BASE_DIR / "data")
)

VECTOR_STORE = Path(
    os.getenv("VECTOR_STORE", BASE_DIR / "vector_store")
)

LOG_FOLDER = BASE_DIR / "logs"

# ------------------------------------------------------------
# Retrieval Configuration
# ------------------------------------------------------------

TOP_K = int(
    os.getenv("TOP_K", 5)
)

SIMILARITY_THRESHOLD = float(
    os.getenv("SIMILARITY_THRESHOLD", 0.70)
)

# ------------------------------------------------------------
# Chunk Configuration
# ------------------------------------------------------------

CHUNK_SIZE = 1000

CHUNK_OVERLAP = 200

# ------------------------------------------------------------
# Embedding Configuration
# ------------------------------------------------------------

EMBEDDING_BATCH_SIZE = 32

# ------------------------------------------------------------
# Streamlit Configuration
# ------------------------------------------------------------

PAGE_TITLE = "📄 PDF RAG Chatbot"

PAGE_ICON = "🤖"

# ------------------------------------------------------------
# Create Required Folders Automatically
# ------------------------------------------------------------

DATA_FOLDER.mkdir(exist_ok=True)

VECTOR_STORE.mkdir(exist_ok=True)

LOG_FOLDER.mkdir(exist_ok=True)
