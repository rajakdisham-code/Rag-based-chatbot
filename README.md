# 🤖 PDF RAG Chatbot

A production-ready **Retrieval-Augmented Generation (RAG)** chatbot that allows users to ask questions from a collection of PDF documents using **Google Gemini**, **FAISS**, and **Sentence Transformers**.

The chatbot extracts text from PDFs, converts it into semantic embeddings, stores them in a FAISS vector database, retrieves the most relevant context, and generates accurate answers using Google's Gemini LLM.

---

## ✨ Features

- 📄 Chat with multiple PDF documents
- 🔍 Semantic search using FAISS
- 🧠 Sentence Transformer embeddings (BGE)
- 🤖 Google Gemini for answer generation
- ⚡ Fast local vector database
- 💬 Streamlit-based chat interface
- 🔄 Easy document ingestion
- 📁 Modular project structure
- 🚀 Ready for Streamlit Community Cloud deployment

---

## 🏗️ Architecture

```
                 PDF Documents
                       │
                       ▼
                PDF Text Extraction
                       │
                       ▼
                 Text Chunking
                       │
                       ▼
          Sentence Transformer Embeddings
                       │
                       ▼
                  FAISS Vector Store
                       │
          User Question
                       │
                       ▼
             Semantic Similarity Search
                       │
                       ▼
             Relevant Context Retrieved
                       │
                       ▼
                 Google Gemini LLM
                       │
                       ▼
                 Final AI Response
```

---

## 📂 Project Structure

```
CHATBOTMAKING/

│── app.py
│── ingest.py
│── requirements.txt
│── README.md
│── .env
│── .gitignore
│
├── core/
│   ├── chunker.py
│   ├── config.py
│   ├── embeddings.py
│   ├── generator.py
│   ├── logger.py
│   ├── pdf_loader.py
│   ├── rag.py
│   ├── retriever.py
│   └── vector_store.py
│
├── ui/
│   ├── chat.py
│   ├── home.py
│   ├── sidebar.py
│   └── styles.py
│
├── data/
├── vector_store/
└── logs/
```

---

## 🛠️ Technologies Used

| Technology | Purpose |
|------------|---------|
| Python | Backend |
| Streamlit | Web Interface |
| Google Gemini | Large Language Model |
| Sentence Transformers | Text Embeddings |
| FAISS | Vector Database |
| PyPDF | PDF Processing |
| NumPy | Numerical Computation |

---

## 🚀 Installation

### Clone Repository

```bash
git clone https://github.com/YOUR_USERNAME/pdf-rag-chatbot.git

cd pdf-rag-chatbot
```

---

### Create Virtual Environment

```bash
python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux / macOS

```bash
source venv/bin/activate
```

---

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

### Configure API Key

Create a `.env` file.

```env
GOOGLE_API_KEY=YOUR_API_KEY
```

---

### Add PDF Documents

Place your PDF files inside

```
data/
```

---

### Build the Vector Database

```bash
python ingest.py
```

---

### Run the Chatbot

```bash
streamlit run app.py
```

---

## 💡 Example Questions

- What is Object-Oriented Programming?
- Explain Inheritance.
- Summarize Chapter 2.
- What are the counselling cutoffs?
- What are the eligibility criteria?
- Compare two colleges.

---

## ⚙️ How It Works

1. PDFs are loaded from the `data/` folder.
2. Text is extracted page by page.
3. Text is split into manageable chunks.
4. Each chunk is converted into embeddings.
5. Embeddings are stored in a FAISS vector database.
6. User questions are embedded.
7. Similar chunks are retrieved.
8. Retrieved context is sent to Gemini.
9. Gemini generates the final answer.

---

## 📸 Screenshots

### Home Page

> Add screenshot here

---

### Chat Interface

> Add screenshot here

---

## 🔮 Future Improvements

- Incremental indexing
- Hybrid Search (BM25 + FAISS)
- Cross-Encoder Reranking
- Streaming responses
- Dark Mode
- PDF Upload from UI
- Authentication
- Conversation History
- Docker Support
- Multi-user deployment

---

## 🤝 Contributing

Contributions, feature requests, and suggestions are welcome.

Feel free to fork the repository and open a Pull Request.

---

## 📜 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

**Hitesh Rajak**

B.Tech, IIT Bombay

Interested in AI, Machine Learning, NLP, RAG Systems, and Backend Development.

GitHub: https://github.com/YOUR_USERNAME

LinkedIn: https://linkedin.com/in/YOUR_PROFILE