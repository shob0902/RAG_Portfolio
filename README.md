<div align="center">

# ✦ Portfolio RAG Assistant ✦

### *A retrieval-augmented brain for a personal portfolio.*

<img src="https://img.shields.io/badge/status-active-6C63FF?style=for-the-badge&labelColor=0d0d0d" />
<img src="https://img.shields.io/badge/python-3.10+-6C63FF?style=for-the-badge&logo=python&logoColor=white&labelColor=0d0d0d" />
<img src="https://img.shields.io/badge/vector%20db-FAISS-6C63FF?style=for-the-badge&labelColor=0d0d0d" />
<img src="https://img.shields.io/badge/LLM-Ollama-6C63FF?style=for-the-badge&labelColor=0d0d0d" />

```
   .    ·    ✦        .          ·          ✦    .
        ┌──────────────────────────────────┐
   ·    │   ask → retrieve → ground → reply │    ·
        └──────────────────────────────────┘
   ✦    .          ·        .    ✦    .    ·
```

</div>

---

## ✦ Overview

**Portfolio RAG Assistant** is a self-hosted Retrieval-Augmented Generation system built to answer questions about a personal portfolio — projects, skills, and experience — with grounded, source-backed responses instead of generic LLM guesswork.

It ingests raw text from `data/`, chunks and embeds it, indexes it in **FAISS**, and serves it through a lightweight **Flask** API and terminal chatbot.

> *Ask it things like:*
> - `"What projects has Shobhit worked on?"`
> - `"What is his experience in computer vision?"`
> - `"What tools does he use for full-stack development?"`

---

## ✦ How it works

```
 data/*.txt
     │
     ▼
 ┌─────────────┐     ┌───────────────┐     ┌────────────────┐
 │   Loader    │ ──▶ │   Splitter    │ ──▶ │   Embeddings    │
 │ loaders.py  │     │ splitter.py   │     │ embeddings.py   │
 └─────────────┘     └───────────────┘     └────────────────┘
                                                     │
                                                     ▼
                                          ┌────────────────────┐
                                          │   FAISS Vector DB   │
                                          │    vector_db/       │
                                          └────────────────────┘
                                                     │
                          user query ────────────────┤
                                                     ▼
                                         ┌─────────────────────┐
                                         │  Retriever + Chain   │
                                         │ retriever.py / chain │
                                         └─────────────────────┘
                                                     │
                                                     ▼
                                          ┌───────────────────┐
                                          │       LLM          │
                                          │      llm.py         │
                                          └───────────────────┘
                                                     │
                                                     ▼
                                            grounded response
```

1. Documents load from `data/`
2. Text is chunked for optimal retrieval
3. Chunks are embedded with a sentence-transformer model
4. Embeddings are stored in **FAISS**
5. On query → retrieve relevant chunks → pass as context to the LLM → generate a grounded answer

---

## ✦ Project structure

```
portfolio-rag-assistant/
├── app.py                 → Flask API for the portfolio assistant
├── build_index.py         → builds the vector index
├── chatbot.py              → interactive terminal chatbot
├── data/                    → source documents used for indexing
├── vector_db/                → generated FAISS index files
└── rag/                        → core RAG pipeline
    ├── config.py                 → configuration & environment variables
    ├── loaders.py                 → document loading logic
    ├── splitter.py                 → chunking logic
    ├── embeddings.py                → embedding model setup
    ├── indexer.py                     → FAISS index creation & storage
    ├── retriever.py                    → retrieval logic
    ├── chain.py                          → orchestration of retrieval + generation
    ├── llm.py                              → LLM integration
    └── prompt_builder.py                    → prompt construction
```

---

## ✦ Getting started

### 1 · Create and activate a virtual environment

```bash
python -m venv venv
source venv/bin/activate
```

<details>
<summary>Windows PowerShell</summary>

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

</details>

### 2 · Install dependencies

```bash
pip install -r requirements.txt
```

### 3 · Build the vector index

```bash
python build_index.py
```

This creates or updates the vector database under `vector_db/`.

---

## ✦ Running it

| Interface | Command | URL |
|---|---|---|
| **Flask backend** | `python app.py` | `http://localhost:5000` |
| **Terminal chatbot** | `python chatbot.py` | — |

---

## ✦ API reference

<table>
<tr><td><b>Health check</b></td><td><code>GET /</code></td></tr>
<tr><td><b>Chat</b></td><td><code>POST /api/chat</code></td></tr>
<tr><td><b>Clear memory</b></td><td><code>POST /api/clear</code></td></tr>
</table>

**Chat request body**

```json
{
  "message": "What projects has Shobhit worked on?"
}
```

---

## ✦ Configuration

Environment variables are defined via `rag/config.py` and `.env`:

| Variable | Purpose |
|---|---|
| `EMBEDDING_MODEL` | sentence-transformer model used for embeddings |
| `CHUNK_SIZE` | size of each text chunk |
| `CHUNK_OVERLAP` | overlap between consecutive chunks |
| `TOP_K` | number of chunks retrieved per query |
| `OLLAMA_MODEL` | local LLM model name |
| `OLLAMA_BASE_URL` | base URL for the Ollama server |
| `TEMPERATURE` | LLM sampling temperature |
| `MAX_TOKENS` | max tokens generated per response |

---

## ✦ Notes

- Built for local, document-based RAG — well suited to portfolio-style knowledge bases.
- Make sure your LLM backend is running (e.g. **Ollama**, locally) before starting the app.
- Rebuild `vector_db/` whenever the source documents in `data/` change.

---

## ✦ Roadmap

- [ ] Hybrid search — keyword + vector retrieval
- [ ] Reranking for sharper context selection
- [ ] Persistent chat history
- [ ] Support for more document formats
- [ ] Cloud deployment

---

<div align="center">

```
   ·    .    ✦   built by Shobhit   ✦    .    ·
```

</div>