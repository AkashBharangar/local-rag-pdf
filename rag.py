from langchain_chroma import Chroma
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

from utils.embeddings import get_embedding_model
from config import GROQ_API_KEY, CHROMA_DIR

embedding = get_embedding_model()

vector_store = Chroma(
    persist_directory=str(CHROMA_DIR),
    embedding_function=embedding
)

retriever = vector_store.as_retriever(
    search_type= "similarity",
    search_kwargs= {"k": 3}
)

prompt = ChatPromptTemplate.from_template(
    """You are an AI assistant
    Answer the user's questions using ONLY the give context.
    if you don't know the answer, just say that.
    
    context:
    {context}
    Question:
    {question}
    Answer:"""
)

llm = ChatGroq(
    model="llama-3.3-70b-versatile",
    temperature=0,
    api_key=GROQ_API_KEY
)

output_parser = StrOutputParser()


def get_answer(question: str) -> str:
    """Answer the question from retrieving the context from vector database"""

    docs = retriever.invoke(question)

    context ="\n\n".join(doc.page_content for doc in docs)

    chain = prompt | llm | output_parser

    response = chain.invoke(
        {"context": context,
        "question": question}
    )

    return response