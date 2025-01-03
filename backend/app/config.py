import os
from dotenv import load_dotenv

load_dotenv()  # This will populate os.environ with variables from .env
GEMINI_API_KEY = os.environ.get("GEMINI_API_KEY") 