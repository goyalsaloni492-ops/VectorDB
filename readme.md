# 🚀 VectorEngine — High-Performance Vector Database & RAG System in C++

A production-inspired **Vector Database** implemented from scratch in **C++**, featuring multiple nearest-neighbor search algorithms, Retrieval-Augmented Generation (RAG), and a modern web interface powered by a local Large Language Model (LLM) using Ollama.

---

## 📌 Overview

This project demonstrates the core concepts behind modern vector databases such as **Pinecone**, **Weaviate**, **Milvus**, and **Chroma** by implementing the underlying algorithms from scratch.

It supports semantic search, document embedding, and local RAG while allowing users to benchmark multiple search algorithms in real time.

---

## ✨ Features

- 🔍 Approximate Nearest Neighbor Search using **HNSW**
- 🌳 Exact Search using **KD-Tree**
- ⚡ Brute Force Search Benchmark
- 📏 Cosine, Euclidean and Manhattan distance metrics
- 🤖 Retrieval-Augmented Generation (RAG)
- 🧠 Local embeddings using **nomic-embed-text**
- 💬 Local LLM responses using **llama3.2**
- 📈 Interactive 2D PCA Visualization
- 🌐 REST API Server
- 📚 Document Chunking & Embedding
- 📊 Algorithm Performance Comparison

---

## 🏗️ System Architecture

```
                User Query
                     │
                     ▼
             Ollama Embeddings
                     │
                     ▼
          Vector Database (C++)
      ┌─────────┬──────────┬──────────┐
      │  HNSW   │ KD-Tree  │BruteForce│
      └─────────┴──────────┴──────────┘
                     │
                     ▼
          Top-K Relevant Documents
                     │
                     ▼
            Ollama (llama3.2)
                     │
                     ▼
             Generated Response
```

---

## 🛠 Tech Stack

| Category | Technology |
|----------|------------|
| Language | C++17 |
| Backend | cpp-httplib |
| AI Models | Ollama |
| Embedding Model | nomic-embed-text |
| LLM | llama3.2 |
| Algorithms | HNSW, KD-Tree, Brute Force |
| Frontend | HTML, CSS, JavaScript |
| Visualization | PCA Scatter Plot |

---

## 📂 Project Structure

```
VectorDB/
│
├── main.cpp
├── httplib.h
├── index.html
├── README.md
└── db.exe
```

---

## 🚀 Getting Started

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/VectorDB.git
cd VectorDB
```

### Install Requirements

- MSYS2
- Git
- Ollama

Download models

```powershell
ollama pull nomic-embed-text
ollama pull llama3.2
```

### Compile

```bash
g++ -std=c++17 -O2 main.cpp -o db.exe -lws2_32
```

### Run

Start Ollama

```powershell
ollama serve
```

Start VectorDB

```powershell
./db.exe
```

Open

```
http://localhost:8080
```

---

## 📊 Implemented Algorithms

| Algorithm | Complexity |
|------------|------------|
| Brute Force | O(N) |
| KD-Tree | O(log N) (Low Dimensions) |
| HNSW | Approx. O(log N) |

---

## 🎯 Learning Outcomes

This project demonstrates:

- Vector Database Design
- Approximate Nearest Neighbor Search
- Similarity Search
- Information Retrieval
- Retrieval-Augmented Generation
- Local LLM Integration
- REST API Development
- High Performance C++ Programming

---

## 📷 Demo

<img width="100%" src="docs/demo.png">

*(Replace with your own screenshot.)*

---

## 📈 Future Improvements

- PDF Upload Support
- Persistent Vector Storage
- Hybrid Search
- Streaming Responses
- Docker Deployment
- Authentication
- FAISS Benchmark Comparison
- Multi-user Support

---

## ⭐ If you found this project useful, consider giving it a star.
