# app/routers/documents.py
import os
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends, status
from sqlalchemy.orm import Session
from app.database.connection import get_db
from app.database.models import Document
from app.services.pdf_processor import extract_text_from_pdf
from app.services.nlp_service import embed_pdf_text_into_chroma

router = APIRouter(tags=["Documents"])

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...), db: Session = Depends(get_db)):
    # ✅ Validate file type
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported."
        )

    # ✅ Ensure uploads directory exists
    os.makedirs("uploads", exist_ok=True)
    file_location = os.path.join("uploads", file.filename)

    # ✅ Save uploaded PDF safely
    try:
        with open(file_location, "wb") as f:
            content = await file.read()
            f.write(content)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Failed to save PDF: {e}")

    # ✅ Extract text
    pdf_text = extract_text_from_pdf(file_location)
    if not pdf_text or not pdf_text.strip():
        raise HTTPException(status_code=400, detail="No text extracted from PDF.")

    # ✅ Store metadata in DB
    document = Document(filename=file.filename, text_content=pdf_text)
    db.add(document)
    db.commit()
    db.refresh(document)

    # ✅ Embed in Chroma (vector store)
    try:
        embed_pdf_text_into_chroma(pdf_text)
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Embedding failed: {e}")

    return {
        "message": "Uploaded successfully",
        "document_id": document.id,
        "filename": file.filename
    }
