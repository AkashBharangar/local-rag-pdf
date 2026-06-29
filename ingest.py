from config import DATA_DIR, CHROMA_DIR
from utils.loader import load_documents
from utils.splitter import split_documents
from utils.embeddings import get_embedding_model

from langchain_chroma import Chroma


def main():
    print("Loading PDFs...")
    documents = load_documents(DATA_DIR)

    print(f"Loaded {len(documents)} pages")

    print("Splitting documents...")
    chunks = split_documents(documents)

    print(f"Created {len(chunks)} chunks")

    print("Creating embeddings...")

    embeddings = get_embedding_model()

    print("Saving to ChromaDB...")

    Chroma.from_documents(
        documents=chunks,
        embedding=embeddings,
        persist_directory=str(CHROMA_DIR)
    )

    print("Done!")


if __name__ == "__main__":
    main()