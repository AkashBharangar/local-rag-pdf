from langchain_community.document_loaders import PyMuPDFLoader
from pathlib import Path

def load_documents(data_dir: Path):
    """Load all PDf files from data directory"""

    documents = []

    for pdf_file in data_dir.glob("*.pdf"):
        loader = PyMuPDFLoader(str(pdf_file))
        documents.extend(loader.load())

    return documents