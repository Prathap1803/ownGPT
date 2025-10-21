from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from typing import Optional
import requests
import os
import json

app = FastAPI()

# Enable CORS so frontend can talk to backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Set specific origin in production
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Serve index.html (chat UI) from same directory
@app.get("/")
def serve_index():
    return FileResponse("index.html")

# Request body schema
class ChatRequest(BaseModel):
    message: str
    model: Optional[str] = "dolphin-mistral:latest"

# Chat endpoint: streams response from Ollama to frontend
@app.post("/chat")
async def chat(request: ChatRequest):
    def stream_response():
        url = "http://localhost:11434/api/generate/"
        payload = {
            "model": request.model,
            "prompt": request.message,
            "stream": True
        }

        try:
            with requests.post(
                url, 
                json=payload, 
                stream=True
                ) as response:
                response.raise_for_status()
                for line in response.iter_lines():
                    if line:
                        chunk = json.loads(line)
                        yield chunk.get("response", "")
        except Exception as e:
            yield f"\n❌ Error: {str(e)}"

    return StreamingResponse(stream_response(), media_type="text/plain")

@app.get("/models")
def list_models():
    try:
        response = requests.get("http://localhost:11434/api/tags")
        response.raise_for_status()
        data = response.json()
        models = [model["name"] for model in data.get("models", [])]
        return {"models": models}
    except Exception as e:
        return {"error": str(e), "models": []}



# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
