# 🍕 Pizza Restaurant QA System

## 📖 Introduction
This project demonstrates how to build a **question-answering system** for a pizza restaurant using **LangChain**, **Ollama models**, and a **vector database**.  
The system is designed to retrieve relevant customer reviews from a dataset and generate natural-language answers to user questions.  

By combining **embeddings, retrieval, and LLM reasoning**, the application allows users to ask about restaurant experiences, customer satisfaction, and other insights directly from real review data.

---

## ⚙️ Implementation

### 1. Data Preparation
- Input dataset: `realistic_restaurant_reviews.csv` (contains review text, rating, date, and title).  
- Reviews are transformed into `Document` objects with **page content** and **metadata**.

### 2. Embedding & Vector Store (`vector.py`)
- Embeddings are created using **OllamaEmbeddings** with the `mxbai-embed-large` model.  
- A **Chroma vector database** stores these embeddings.  
- If the database doesn’t exist, documents are embedded and persisted automatically.  
- A retriever (`retriever`) is defined to return the top 5 most relevant reviews per query.

### 3. Prompt & Model (`main.py`)
- Defines a **ChatPromptTemplate** that injects retrieved reviews into the model context.  
- Uses **OllamaLLM** (`llama3.2`) to generate responses.  
- The prompt structure:  
You are an expert in answering questions about a pizza restaurant.
Here are some relevant reviews: {reviews}
Here is the question to answer: {question}

markdown
Copy code
- A loop allows interactive questioning until the user quits (`q`).

### 4. Retrieval + Generation Workflow
1. User enters a question.  
2. Retriever pulls top 5 relevant reviews.  
3. Reviews are formatted with metadata (ID, rating, date).  
4. LLM produces a response combining retrieved context and reasoning.  

---

## 📊 Results
- The system successfully retrieves relevant customer reviews based on semantic similarity.  
- Responses from the model include both **factual review content** and **summarized reasoning**, making them useful for:  
- Customer service analysis  
- Business intelligence  
- Restaurant feedback summarization  

**Example**  
- **Question:** *“How do customers feel about the service?”*  
- **System Answer:** A synthesized response highlighting patterns in the reviews about staff friendliness, wait times, or customer complaints.  

---

## ✅ Conclusion
This project demonstrates a **retrieval-augmented generation (RAG)** pipeline applied to a real-world scenario — analyzing restaurant reviews.  

- **Strengths:**  
- Efficient review search via vector embeddings.  
- Natural-language answers tailored to user queries.  
- Easily extendable to other domains (e.g., hotels, e-commerce, support tickets).  

- **Future Improvements:**  
- Add more advanced filtering (by rating/date).  
- Expand dataset with multi-source reviews.  
- Integrate a web UI for non-technical users.  

Overall, the project shows how **LLMs + retrieval** can transform raw text data into actionable insights.  
