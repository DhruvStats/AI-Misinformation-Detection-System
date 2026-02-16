from backend.db import init_db, log_prediction
import time
from fastapi import FastAPI
from pydantic import BaseModel
import httpx

app = FastAPI()
init_db()
class RequestData(BaseModel):
    text: str

@app.post("/predict")
async def predict(data: RequestData):
    start_time = time.time()

    async with httpx.AsyncClient(timeout=None) as client:
        response = await client.post(
            "http://127.0.0.1:11434/api/chat",
            json={
                "model": "llama3",
                "stream": False,
                "messages": [
                    {
                        "role": "system",
                        "content": "You are a fake news detection assistant. Reply only with 'Real News' or 'Fake News' and give short reason."
                    },
                    {"role": "user", "content": data.text}
                ]
            }
        )

    result = response.json()
    prediction = result["message"]["content"]

    end_time = time.time()
    response_time = round(end_time - start_time, 3)

    # 🔥 Log to database
    log_prediction(data.text, prediction, response_time)

    return {
        "prediction": prediction,
        "response_time_seconds": response_time
    }