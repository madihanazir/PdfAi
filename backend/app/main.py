from fastapi import FastAPI
from app.routers import documents, questions
from fastapi.middleware.cors import CORSMiddleware
from app.database import connection
from app.database import models  
import logging
models.Base.metadata.create_all(bind=connection.engine)


logging.basicConfig(level=logging.DEBUG)

app = FastAPI()

# Add CORS middleware with full URLs
app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "https://pdf-ai-nu.vercel.app",     # your deployed frontend
        "http://localhost:5173",            # your local dev frontend
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])

@app.get("/")
def read_root():
    return {"message": "Hello from Madiha"}
