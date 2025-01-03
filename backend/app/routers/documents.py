# app/routers/documents.py
import os
from fastapi import APIRouter, File, UploadFile, HTTPException, Depends, status
from app.database.connection import get_db
from app.database.models import Document
from app.services.pdf_processor import extract_text_from_pdf
from app.services.nlp_service import embed_pdf_text_into_chroma

router = APIRouter()

@router.post("/upload")
async def upload_pdf(file: UploadFile = File(...), db=Depends(get_db)):
    if not file.filename.lower().endswith(".pdf"):
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Only PDF files are supported."
        )

    # 1. Save the PDF
    os.makedirs("uploads", exist_ok=True)
    file_location = f"uploads/{file.filename}"
    with open(file_location, "wb") as f:
        f.write(await file.read())

    # 2. Extract text
    pdf_text = extract_text_from_pdf(file_location)
    if not pdf_text.strip():
        raise HTTPException(400, "No text extracted from PDF")

    # 3. Store metadata in DB
    document = Document(filename=file.filename, text_content=pdf_text)
    db.add(document)
    db.commit()
    db.refresh(document)

    # 4. Embed text in Chroma for retrieval-based Q&A
    embed_pdf_text_into_chroma(pdf_text)

    return {"message": "Uploaded successfully", "document_id": document.id}
