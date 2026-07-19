"""
===========================================
Portfolio AI Configuration
===========================================
This file stores all configurable settings
used throughout the project.
Changing values here updates the entire
application without modifying other files.
"""
from pathlib import Path
from dotenv import load_dotenv
import os
# ==========================================
# Load Environment Variables
# ==========================================
load_dotenv()
# ==========================================
# Project Paths
# ==========================================
# portfolio-ai/
BASE_DIR = Path(__file__).resolve().parent.parent
# Dataset folder
DATA_PATH = BASE_DIR / "data"
# Vector database folder
VECTOR_DB_PATH = BASE_DIR / "vector_db"
# ==========================================
# Embedding Model
# ==========================================
EMBEDDING_MODEL = os.getenv(
    "EMBEDDING_MODEL",
    "sentence-transformers/all-MiniLM-L6-v2"
)
# ==========================================
# Text Chunking
# ==========================================
CHUNK_SIZE = int(
    os.getenv("CHUNK_SIZE", 600)
)
CHUNK_OVERLAP = int(
    os.getenv("CHUNK_OVERLAP", 100)
)
# ==========================================
# Retriever
# ==========================================
TOP_K = int(os.getenv("TOP_K", 4))
FETCH_K = int(os.getenv("FETCH_K", 20))
MMR_LAMBDA = float(os.getenv("MMR_LAMBDA", 0.5))
# ==========================================
# Ollama Configuration
# ==========================================
OLLAMA_MODEL = os.getenv(
    "OLLAMA_MODEL",
    "llama3.1"
)
OLLAMA_BASE_URL = os.getenv(
    "OLLAMA_BASE_URL",
    "http://localhost:11434"
)
# ==========================================
# Generation Settings
# ==========================================
TEMPERATURE = float(
    os.getenv("TEMPERATURE", 0.2)
)
MAX_TOKENS = int(
    os.getenv("MAX_TOKENS", 1024)
)
# ==========================================
# Flask Server
# ==========================================
HOST = os.getenv(
    "HOST",
    "0.0.0.0"
)
PORT = int(
    os.getenv("PORT", 5000)
)
DEBUG = os.getenv(
    "DEBUG",
    "True"
).lower() == "true"
# ==========================================
# Conversation Memory
# ==========================================
MAX_HISTORY = int(
    os.getenv("MAX_HISTORY", 10)
)
# ==========================================
# Logging
# ==========================================
LOG_LEVEL = os.getenv(
    "LOG_LEVEL",
    "INFO"
)