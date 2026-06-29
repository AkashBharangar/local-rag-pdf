![Python](https://img.shields.io/badge/Python-3.10-blue)
![Groq](https://img.shields.io/badge/LLM-Groq-purple)
![Llama](https://img.shields.io/badge/Model-Llama_3.3_70B-green)
![ChromaDB](https://img.shields.io/badge/VectorDB-ChromaDB-blue)
![LangChain](https://img.shields.io/badge/Framework-LangChain-success)
![RAG](https://img.shields.io/badge/AI-Retrieval_Augmented_Generation-orange)
![Embeddings](https://img.shields.io/badge/Embeddings-HuggingFace-red)

# 📚 Local PDF RAG

A production-ready **Retrieval-Augmented Generation (RAG)** application built using **Python**, **Groq API**, **Llama 3.3**, **LangChain**, **ChromaDB**, and **HuggingFace Embeddings**.

The application converts PDF documents into a searchable vector database and enables users to ask natural language questions grounded in the document content using semantic retrieval and LLM-powered answer generation.

This project demonstrates the complete RAG pipeline used in modern AI applications, including document ingestion, chunking, embeddings, vector search, retrieval, prompt engineering, and LLM inference.

---

# 🚀 Features

- 📄 Load one or multiple PDF documents
- ✂️ Intelligent document chunking
- 🧠 Local HuggingFace Embeddings
- 🗄️ ChromaDB Vector Database
- 🔍 Semantic Similarity Search
- 📚 Retrieval-Augmented Generation (RAG)
- 🤖 Groq Llama 3.3 Integration
- 💬 Interactive CLI Chat Interface
- ⚡ Fast Vector Retrieval
- 🧩 Modular Project Architecture
- 🔐 Secure API Key Management using Environment Variables

---

# 🏗️ Architecture

```text
                    PDF Documents
                          │
                          ▼
                PyMuPDF Document Loader
                          │
                          ▼
          Recursive Character Text Splitter
                          │
                          ▼
           HuggingFace Embedding Model
                          │
                          ▼
                Chroma Vector Database
                          │
                    User Question
                          │
                          ▼
               Embed User Question
                          │
                          ▼
             Semantic Similarity Search
                          │
                          ▼
              Retrieve Top-K Chunks
                          │
                          ▼
         Prompt Engineering with Context
                          │
                          ▼
             Groq (Llama 3.3 70B)
                          │
                          ▼
                  Grounded AI Answer
```

---

# 📂 Project Structure

```text
local-pdf-rag/
│
├── data/                     # PDF documents
├── chroma_db/                # Vector database (generated)
│
├── utils/
│   ├── loader.py             # PDF loading
│   ├── splitter.py           # Document chunking
│   └── embeddings.py         # Embedding model
│
├── ingest.py                 # Creates ChromaDB
├── rag.py                    # Retrieval pipeline
├── app.py                    # CLI interface
├── config.py                 # Configuration
│
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

---

# 🛠️ Tech Stack

| Component | Technology |
|------------|------------|
| Language | Python |
| LLM Provider | Groq API |
| Model | Llama 3.3 70B Versatile |
| Framework | LangChain |
| Vector Database | ChromaDB |
| Embeddings | HuggingFace Sentence Transformers |
| PDF Loader | PyMuPDF |
| Text Splitting | RecursiveCharacterTextSplitter |
| Environment Variables | python-dotenv |

---

# 📦 Installation

## 1. Clone Repository

```bash
git clone https://github.com/your-username/local-pdf-rag.git

cd local-pdf-rag
```

---

## 2. Create Virtual Environment

```bash
python -m venv venv
```

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

# 🔑 Environment Setup

Create a `.env` file.

```env
GROQ_API_KEY=your_groq_api_key
```

---

# 📄 Add PDFs

Place your PDF files inside:

```text
data/
```

---

# 🏗️ Build the Vector Database

Run:

```bash
python ingest.py
```

This will:

- Load PDFs
- Split text into chunks
- Generate embeddings
- Store vectors inside ChromaDB

---

# ▶️ Run the Application

```bash
python app.py
```

Example:

```text
You:
What is Retrieval Augmented Generation?

Assistant:
Retrieval-Augmented Generation (RAG) is...
```

---

# 💡 How It Works

1. Load PDF documents.
2. Extract text using PyMuPDF.
3. Split documents into overlapping chunks.
4. Generate embeddings using HuggingFace.
5. Store embeddings in ChromaDB.
6. User asks a question.
7. The question is embedded.
8. ChromaDB retrieves the most relevant chunks.
9. Retrieved context is inserted into a prompt.
10. Groq's Llama 3.3 generates a grounded response.

---

# 🧠 Key Concepts Learned

## 📄 PDF Processing

Extracting structured text from PDF documents.

## ✂️ Text Chunking

Breaking large documents into overlapping chunks for better retrieval.

## 🧠 Embeddings

Converting text into dense vector representations for semantic similarity.

## 🗄️ Vector Database

Efficient storage and retrieval of document embeddings using ChromaDB.

## 🔍 Semantic Search

Finding relevant information based on meaning instead of keyword matching.

## 📚 Retrieval-Augmented Generation (RAG)

Combining retrieval with LLM inference to generate grounded answers.

## 🤖 LLM Integration

Using Groq's ultra-fast inference API with Llama 3.3.

## 🧠 Prompt Engineering

Injecting retrieved context into prompts to reduce hallucinations.

## 🏗️ Modular AI Applications

Separating ingestion, retrieval, embeddings, and inference into reusable components.

---

# 🚀 Future Improvements

- 📑 Source citations (PDF & page numbers)
- 🎯 Metadata filtering
- 🔀 Hybrid Search (Keyword + Semantic)
- 📈 MMR Retrieval
- 💬 Conversation Memory
- 🌐 Streamlit Web Interface
- ⚡ FastAPI REST API
- 🐳 Docker Support
- ☁️ Cloud Deployment
- 📚 Multi-user document collections

---

# ⚠️ Limitations

- Supports PDF documents only.
- Requires rebuilding the vector database when documents change.
- Responses depend on retrieval quality.
- Internet connection required for Groq API inference.

---

# 📚 Learning Outcomes

After building this project, you understand:

- Retrieval-Augmented Generation (RAG)
- Vector databases
- Semantic search
- Embeddings
- ChromaDB
- LangChain
- HuggingFace Embeddings
- Prompt Engineering
- Groq API integration
- LLM application architecture
- Document Question Answering
- Modular AI system design

---

# 🤝 Contributing

Contributions are welcome!

Possible improvements:

- Better retrieval strategies
- Improved prompt templates
- UI development
- Additional document formats
- Multi-model support
- Performance optimization

---

# ⭐ Acknowledgements

- Groq for ultra-fast LLM inference
- Meta for the Llama models
- LangChain for orchestration
- ChromaDB for vector storage
- HuggingFace for embedding models
- PyMuPDF for PDF parsing

---

# 👨‍💻 Author

Built as a hands-on learning project while exploring **Retrieval-Augmented Generation (RAG)**, **Large Language Models (LLMs)**, **Vector Databases**, **Semantic Search**, **Prompt Engineering**, and **Production-Ready AI Systems**.