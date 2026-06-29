import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv()

BASE_DIR = Path(__file__).parent
DATA_DIR = BASE_DIR/"data"
CHROMA_DIR = BASE_DIR/"chroma_db"

GROQ_API_KEY = os.getenv("GROQ_API_KEY")

embedding_model = "sentence-transformers/all-MiniLM-L6-v2"

CHUNK_SIZE = 1000
CHUNK_OVERLAP = 200