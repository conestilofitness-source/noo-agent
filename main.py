from fastapi import FastAPI
from starlette.responses import Response
import json

app = FastAPI()


@app.get("/")
def root():
    payload = {
        "agent": "NÓO",
        "status": "activo",
        "msg": "NÓO está vivo 🚀"
    }
    return Response(
        content=json.dumps(payload, ensure_ascii=False),
        media_type="application/json; charset=utf-8"
    )


@app.get("/ping")
def ping():
    return {"pong": True}


@app.get("/think")
def think(q: str):
    payload = {
        "question": q,
        "answer": f"NÓO recibió tu pregunta: '{q}' y está pensando 🤖"
    }
    return Response(
        content=json.dumps(payload, ensure_ascii=False),
        media_type="application/json; charset=utf-8"
    )
