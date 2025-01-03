from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain import PromptTemplate
from app.config import GEMINI_API_KEY
import os
import shutil

def build_vectorstore_from_text(document_text: str, persist_dir: str = "./chroma_storage"):
    """
    Build the Chroma vectorstore with embeddings.
    """
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(document_text)

    embed_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )

    vectorstore = Chroma.from_texts(chunks, embed_model, persist_directory=persist_dir)
    vectorstore.persist()
    return vectorstore

def get_retrieval_qa_chain(persist_dir: str = "./chroma_storage"):
    """
    Load Chroma with the embedding function for query retrieval.
    """
    embed_model = GoogleGenerativeAIEmbeddings(
        model="models/embedding-001",
        google_api_key=GEMINI_API_KEY
    )

    vectorstore = Chroma(
        embedding_function=embed_model,  # Pass the embedding function here
        persist_directory=persist_dir
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-pro",
        google_api_key=GEMINI_API_KEY,
        temperature=0.2
    )

    template = """Use the following context to answer the question at the end.
If you don't know, just say 'I don't know'.
{context}
Question: {question}
Answer:"""
    prompt = PromptTemplate.from_template(template)

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        retriever=retriever,
        return_source_documents=True,
        chain_type_kwargs={"prompt": prompt},
    )
    return qa_chain

def answer_question(question: str) -> str:
    """
    Retrieve relevant chunks and get an answer using the retrieval chain.
    """
    chain = get_retrieval_qa_chain("./chroma_storage")
    result = chain({"query": question})
    return result["result"]

def embed_pdf_text_into_chroma(document_text: str) -> None:
    """
    Build and persist the Chroma vector store for the provided document text.
    """
    if os.path.exists("./chroma_storage"):
        shutil.rmtree("./chroma_storage")  # Clear existing data

    build_vectorstore_from_text(document_text, persist_dir="./chroma_storage")