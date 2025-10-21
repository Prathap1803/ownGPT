# 🧠 Local LLM Chat App (FastAPI + Ollama + HTML)

A minimal, full-stack chat application that connects a **FastAPI backend** to a **frontend chat UI**, and streams real-time responses from a **local LLM via Ollama** using the `dolphin-mistral` model.

---

## ✨ Features

- ⚡ Streamed AI responses using Ollama (`dolphin-mistral`)
- 🧑‍💻 Simple HTML/CSS/JS frontend with markdown rendering
- 🚀 FastAPI backend with CORS and live streaming
- 🖥️ Serves `index.html` directly from backend
- 🌐 Easy to deploy locally and customize

---

## 📦 Requirements

- Python 3.8+
- [Ollama](https://ollama.com/) installed and running
- Pull the Dolphin Mistral model:

  ```bash
  ollama pull dolphin-mistral

# 📁 Project Structure
```
.
├── backend.py         # FastAPI backend
├── index.html         # Frontend UI
├── requirements.txt   # Python dependencies
└── README.md
```

# 🛠 Installation

1.Clone the repository:

```
git clone https://github.com/Prathap1803/ownGPT.git
cd local-llm-chat
```


2.Set up a virtual environment (optional):

```
python -m venv venv 
source venv/bin/activate  # On Windows: venv\Scripts\activate
```


3.Install dependencies:

```
pip install -r requirements.txt
```


4.Start Ollama with the model:

```
ollama run dolphin-mistral
```

# ▶️ Running the Server

Start the FastAPI server with:

```
uvicorn backend:app --reload
```


Then open your browser and visit:

```
http://127.0.0.1:8000
```


This will load the local HTML-based chat interface.

# 📡 API Overview
`POST /chat`

Streams a response from the LLM based on user input.

Request Body
```
{
  "message": "Hello, what can you do?"
}
```

Response

A streaming plain text response from the local model.

# 💬 Frontend (index.html)

* Vanilla HTML + CSS + JS (no frameworks)

* Renders streamed responses using marked.js for markdown

* Features:

    * Code block formatting

    * Scrollable chat UI

    * Send on Enter

    * Mobile-friendly layout

# 🌐 CORS

CORS is enabled for all origins during development:

```
allow_origins=["*"]
```


Update this to your frontend's domain before deploying to production.



✅ To-Do (Suggestions)


 [ ] Add model selection in UI

 [ ] Add chat history

 [ ] Add file upload (for context)

 [ ] Dockerize the app
 
