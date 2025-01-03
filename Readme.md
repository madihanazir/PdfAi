Frontend README.md

# PDF QnA App - Frontend

## Overview
This is the frontend of the PDF QnA application, built with React and Tailwind CSS. It allows users to upload PDFs and ask questions about their content.

## Features
- Upload a PDF file.
- Ask questions about the uploaded PDF.
- Responsive design with a clean layout.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/frontend.git

    Navigate to the project directory:

cd frontend

Install dependencies:

npm install

Start the development server:

    npm run dev

    Access the app at http://localhost:5173.

Folder Structure

    src/components/: Contains React components (AskQuestion.jsx, UploadPDF.jsx).
    App.jsx: Main application file.
    index.css: Tailwind CSS styles.

Technologies Used

    React
    Tailwind CSS
    Axios


#### **Backend README.md**
```markdown
# PDF QnA App - Backend

## Overview
This is the backend of the PDF QnA application, built with FastAPI. It handles PDF uploads, processes their content, and provides answers to user questions using a vector database and LLM.

## Features
- Upload PDF files.
- Store extracted content in a database.
- Use vector embeddings for retrieval-based Q&A.

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone https://github.com/your-repo-name/backend.git

    Navigate to the project directory:

cd backend

Create a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

Install dependencies:

pip install -r requirements.txt

Start the FastAPI server:

    uvicorn app.main:app --reload

    Access the API docs at http://127.0.0.1:8000/docs.

Folder Structure

    app/routers/: Contains route handlers (documents.py, questions.py).
    app/services/: NLP and PDF processing logic (nlp_service.py, pdf_processor.py).
    app/database/: Database connection and models.

API Endpoints

    POST /documents/upload: Upload a PDF file.
        Request Body: Form-data with the file.
        Response: { "message": "Uploaded successfully", "document_id": 1 }
    POST /questions/ask: Ask a question about a document.
        Request Body: { "document_id": 1, "question": "What is this about?" }
        Response: { "answer": "This document is about..." }

Technologies Used

    FastAPI
    Chroma (for vector database)
    LangChain (for LLM integration)
    SQLite (for database)


---

### 3. **Brief Architecture Overview**

#### **Architecture Overview**
The application consists of two main components:
1. **Frontend**:
   - Built with React for a responsive and interactive user interface.
   - Users can upload PDFs and ask questions about their content.

2. **Backend**:
   - Built with FastAPI to handle file uploads, content processing, and question answering.
   - Uses a vector database (Chroma) to store document embeddings and retrieve relevant content for questions.
   - Integrates with an LLM for answer generation.

#### **Data Flow**
1. **Upload PDF**:
   - Frontend sends the PDF to the backend (`/documents/upload`).
   - Backend processes the PDF, extracts text, and stores it in the database and vector database.
   - Backend returns the `document_id`.

2. **Ask Question**:
   - Frontend sends the `document_id` and question to the backend (`/questions/ask`).
   - Backend retrieves relevant document content using vector similarity search.
   - LLM generates an answer based on the retrieved content.
   - Backend returns the answer to the frontend.
