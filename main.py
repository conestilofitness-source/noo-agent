from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return {"ok": True, "msg": "NÓO está listo 🚀"}

@app.get("/ping")
def ping():
    return {"pong": True}
