from fastapi import FastAPI, Request
from fastapi.middleware.cors import CORSMiddleware
from models.modelo_local import responder_pergunta

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def root():
    return {"Fortebott": "Online"}

@app.post("/perguntar")
async def perguntar(request: Request):
    dados = await request.json()
    pergunta = dados.get("mensagem")
    resposta = responder_pergunta(pergunta)
    return {"resposta": resposta}
