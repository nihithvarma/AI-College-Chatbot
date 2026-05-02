from flask import Flask, request, jsonify, render_template
from sentence_transformers import SentenceTransformer
import numpy as np
import ollama

app = Flask(__name__)

# Load embedding model
model = SentenceTransformer('all-MiniLM-L6-v2')

# Load data
with open("data.txt", "r", encoding="utf-8") as f:
    texts = f.readlines()

# Create embeddings
embeddings = model.encode(texts)


# 🔍 Retrieve top relevant contexts
def retrieve(query):
    q_embed = model.encode([query])[0]
    scores = np.dot(embeddings, q_embed)

    # Get top 3 relevant lines
    top_indices = np.argsort(scores)[-3:]
    context = "\n".join([texts[i] for i in top_indices])

    return context


# 🤖 Generate answer
def generate_answer(query):
    context = retrieve(query)

    prompt = f"""
You are an AI assistant for HITAM College.
Answer ONLY using the given context.
If the answer is not present, say "I don't know".

Context:
{context}

Question: {query}
"""

    response = ollama.chat(
        model='phi3',
        messages=[{"role": "user", "content": prompt}]
    )

    return response['message']['content']


# 🌐 Routes
@app.route("/")
def home():
    return render_template("index.html")


@app.route("/chat", methods=["POST"])
def chat():
    user_msg = request.json.get("message", "")

    if not user_msg.strip():
        return jsonify({"response": "Please enter a valid question."})

    reply = generate_answer(user_msg)
    return jsonify({"response": reply})


# ▶️ Run app
if __name__ == "__main__":
    app.run(debug=True)