from fastapi import FastAPI
from app.routers import documents, questions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],  # Adjust this to restrict origins if needed
    allow_credentials=True,
    allow_methods=["*"],  # Allow all HTTP methods
    allow_headers=["*"],  # Allow all headers
)
# Include routers from different files
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])

# A simple root endpoint to verify server is running
@app.get("/")
def read_root():
    return {"message": "Hello from amaan"}
