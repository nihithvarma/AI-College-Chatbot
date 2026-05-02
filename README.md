# AI-Powered College Chatbot (RAG-based)

This project is an AI-powered chatbot built using a Retrieval-Augmented Generation (RAG) approach. It provides context-aware responses about HITAM (Hyderabad Institute of Technology and Management) by combining semantic search with a local language model.

---

## Overview

The chatbot retrieves relevant information from a custom dataset and generates accurate answers using a language model. It is designed to reduce generic responses and improve answer quality by grounding outputs in domain-specific data.

---

## Features

* Semantic search using vector embeddings
* Retrieval-Augmented Generation (RAG) pipeline
* Integration with local LLMs via Ollama
* Interactive web interface using HTML, CSS, and JavaScript
* Lightweight and optimized for local execution
* Uses real college data for contextual responses

---

## Tech Stack

### Backend

* Python (Flask)

### Frontend

* HTML, CSS, JavaScript

### AI / Machine Learning

* Sentence Transformers (Hugging Face)
* Vector embeddings (MiniLM)
* RAG architecture

### Language Model

* Ollama (local models such as Phi-3 or Llama)

---

## System Workflow

1. The user submits a query through the web interface
2. The query is converted into a vector embedding
3. The system performs similarity search on stored embeddings
4. Relevant context is retrieved from the dataset
5. The context and query are passed to the language model
6. The model generates a response based on the retrieved information

---

## Project Structure

```
college-chatbot/
│
├── app.py
├── data.txt
├── requirements.txt
├── templates/
│   └── index.html
├── .gitignore
├── LICENSE
└── README.md
```

---

## Installation and Setup

### 1. Clone the repository

```
git clone https://github.com/your-username/ai-college-chatbot.git
cd ai-college-chatbot
```

### 2. Create and activate a virtual environment

```
python -m venv venv
venv\Scripts\activate
```

### 3. Install dependencies

```
pip install -r requirements.txt
```

### 4. Install Ollama

Download from:
https://ollama.com

Run a model:

```
ollama run phi3
```

### 5. Run the application

```
python app.py
```

### 6. Access the application

Open a browser and go to:

```
http://127.0.0.1:5000
```

---

## Example Queries

* What is HITAM?
* What programs are offered?
* What are the placement details?
* What facilities are available?

---

## Key Concepts

* Retrieval-Augmented Generation (RAG)
* Vector embeddings
* Semantic search
* Prompt-based response generation
* Natural Language Processing fundamentals

---

## Future Improvements

* Integration with FAISS for scalable vector search
* User authentication system
* Deployment on cloud platforms
* Voice-based interaction
* Admin interface for dataset management

---

## Author

Avinash B
B.Tech – Computer Science

---

## License

This project is licensed under the MIT License.
