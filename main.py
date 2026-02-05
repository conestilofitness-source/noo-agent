from fastapi import FastAPI
from starlette.responses import Response
import json

app = FastAPI()

@app.get("/")
def root():
    payload = {"ok": True, "msg": "Nóo está listo 🚀"}
    return Response(
        content=json.dumps(payload, ensure_ascii=False),
        media_type="application/json; charset=utf-8"
    )

@app.get("/ping")
def ping():
    return {"pong": True}
