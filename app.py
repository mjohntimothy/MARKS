from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
import openai
import uvicorn

openai.api_key = "your_openai_api_key"

app = FastAPI()

# Allow frontend to communicate with backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/chat")
async def chat(request: Request):
    data = await request.json()
    user_message = data["message"]

    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": user_message}]
    )

    bot_response = response["choices"][0]["message"]["content"]
    return {"response": bot_response}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)
