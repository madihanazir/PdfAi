from fastapi import FastAPI
from app.routers import documents, questions
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()
# Add CORS middleware
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],  
    allow_headers=["*"],  
)
# Include routers from different files
app.include_router(documents.router, prefix="/documents", tags=["documents"])
app.include_router(questions.router, prefix="/questions", tags=["questions"])

# A simple root endpoint to verify server is running
@app.get("/")
def read_root():
    return {"message": "Hello from amaan"}
