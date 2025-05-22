import os
from langchain.document_loaders import PyPDFLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OllamaEmbeddings
from langchain_community.vectorstores import FAISS

UPLOAD_DIR = "uploads"

def get_retriever():
    docs = []
    for filename in os.listdir(UPLOAD_DIR):
        path = os.path.join(UPLOAD_DIR, filename)
        if filename.endswith(".pdf"):
            loader = PyPDFLoader(path)
        elif filename.endswith(".txt"):
            loader = TextLoader(path)
        else:
            continue
        docs.extend(loader.load())

    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
    documents = text_splitter.split_documents(docs)

    embeddings = OllamaEmbeddings()
    vectordb = FAISS.from_documents(documents, embeddings)

    return vectordb.as_retriever()
