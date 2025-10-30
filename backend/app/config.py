import os
from dotenv import load_dotenv

load_dotenv()

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY", "")
CHROMA_DIR = os.getenv("CHROMA_DIR", "./chroma_storage")

if not GEMINI_API_KEY:
    print("⚠️ Warning: GEMINI_API_KEY not found. The app will use local embeddings only.")
