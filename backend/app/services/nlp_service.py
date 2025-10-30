from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_community.vectorstores import Chroma
from langchain.chains import RetrievalQA
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_core.prompts import PromptTemplate
import chromadb
import os
import shutil

# You can keep .env loading if needed
from dotenv import load_dotenv
load_dotenv()
GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

def build_vectorstore_from_text(document_text: str, persist_dir: str = "./chroma_storage"):
    splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    chunks = splitter.split_text(document_text)

    # ✅ Free open-source embedding model
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma.from_texts(chunks, embed_model, persist_directory=persist_dir)
    vectorstore.persist()
    return vectorstore


def get_retrieval_qa_chain(persist_dir: str = "./chroma_storage"):
    embed_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")

    vectorstore = Chroma(embedding_function=embed_model, persist_directory=persist_dir)
    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    # ✅ Keep Gemini free model for Q&A (this still works on free tier)
    llm = ChatGoogleGenerativeAI(
        model="gemini-1.5-flash",
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
    chain = get_retrieval_qa_chain("./chroma_storage")
    result = chain({"query": question})
    return result["result"]


def embed_pdf_text_into_chroma(document_text: str) -> None:
    persist_dir = "./chroma_storage"

    try:
        if os.path.exists(persist_dir):
            client = chromadb.PersistentClient(path=persist_dir)
            client.reset()
    except Exception as e:
        print(f"⚠️ Warning while resetting Chroma: {e}")
        try:
            shutil.rmtree(persist_dir, ignore_errors=True)
        except Exception as inner_e:
            print(f"⚠️ Could not remove Chroma storage manually: {inner_e}")

    build_vectorstore_from_text(document_text, persist_dir=persist_dir)
