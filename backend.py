from fastapi import FastAPI
from fastapi.responses import StreamingResponse, FileResponse
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
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

# Chat endpoint: streams response from Ollama to frontend
@app.post("/chat")
async def chat(request: ChatRequest):
    def stream_response():
        url = "http://localhost:11434/api/generate/"
        payload = {
            "model": "dolphin-mistral:latest",
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


# Run the server
if __name__ == "__main__":
    import uvicorn
    uvicorn.run("backend:app", host="127.0.0.1", port=8000, reload=True)
