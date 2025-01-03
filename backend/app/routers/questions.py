# app/routers/questions.py
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from app.database.connection import get_db
from app.database.models import Document
from app.services.nlp_service import answer_question

router = APIRouter()

class QuestionRequest(BaseModel):
    document_id: int  # We'll just confirm the doc exists
    question: str

@router.post("/ask")
def ask_question(req: QuestionRequest, db=Depends(get_db)):
    # Verify the document ID
    document = db.query(Document).filter(Document.id == req.document_id).first()
    if not document:
        raise HTTPException(status_code=404, detail="Document not found")

    # The text is already embedded in Chroma from the upload step
    # We just pass user question to our chain
    answer = answer_question(req.question)
    return {"answer": answer}
