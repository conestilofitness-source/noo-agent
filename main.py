from fastapi import FastAPI
from fastapi.responses import JSONResponse

app = FastAPI()

@app.get("/")
def root():
    return JSONResponse(
        content={"ok": True, "msg": "Nó está listo 🚀"},
        media_type="application/json; charset=utf-8"
    )
