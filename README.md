# 🍕 Local AI Agent for Pizza Restaurant Reviews (RAG + LangChain)

This project demonstrates how to build a **local Retrieval-Augmented Generation (RAG) AI agent** with **LangChain**.  
The agent processes a CSV file of pizza restaurant reviews and answers natural language questions about the restaurant by retrieving relevant reviews and generating contextual responses.

---

## 📌 Project Overview

- **Data Source:** `realistic_restaurant_reviews.csv` (contains Title, Date, Rating, Review).  
- **Vector Store:** Reviews are embedded with **Ollama embeddings** and stored in a **ChromaDB** database.  
- **RAG Pipeline:** When you ask a question, the system retrieves the most relevant reviews (via vector search) and uses LangChain to generate an answer.  
- **Local Execution:** No cloud dependencies — runs locally using [Ollama](https://ollama.ai) for embeddings.  

---

## ⚙️ Requirements

Install dependencies from `requirements.txt`:

```bash
pip install -r requirements.txt
Contents of requirements.txt:

nginx
Copy code
langchain
langchain-ollama
langchain-chroma
You also need:

Ollama installed locally → Download Ollama

Python 3.9+

📂 Project Structure
bash
Copy code
├── main.py                   # Entry point: AI Agent loop
├── vector.py                 # Builds/loads the vector store from reviews CSV
├── requirements.txt          # Project dependencies
├── realistic_restaurant_reviews.csv   # Input dataset (not included here)
└── README.md                 # Documentation
🚀 Getting Started
Clone this repo:

bash
Copy code
git clone https://github.com/khawagaa/Local_AI_Agent_using_Langchain_and_RAG.git
cd <repo-name>
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Prepare Ollama embeddings:
Ensure Ollama is installed and running locally.

Run the project:

bash
Copy code
python main.py
Ask questions!
Example queries:

“What do people say about the pizza crust?”

“How was the service rated in recent reviews?”

“Summarize customer opinions on delivery time.”

🔍 How It Works
Data Loading:

vector.py reads realistic_restaurant_reviews.csv.

Each review (Title + Review text) is turned into a Document with metadata (Rating, Date).

Embedding & Storage:

Documents are embedded with OllamaEmbeddings.

Stored in a persistent ChromaDB database.

Retriever:

Retrieves the top k=5 relevant reviews for a query.

LangChain Agent:

Uses the retriever results to ground its answers in real data.

📖 References
LangChain Documentation

ChromaDB

Ollama

LangChain + RAG Guide

