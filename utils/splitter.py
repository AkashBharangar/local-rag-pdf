from langchain_text_splitters import RecursiveCharacterTextSplitter
from config import CHUNK_OVERLAP, CHUNK_SIZE

def split_documents(documents):
    """Split the documents according to chunk size and chunk overlap"""

    splitter = RecursiveCharacterTextSplitter(
        chunk_size = CHUNK_SIZE,
        chunk_overlap = CHUNK_OVERLAP
    )

    return splitter.split_documents(documents)