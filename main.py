from fastapi import FastAPI
from models import TransationType
from fastapi import HTTPException
from datetime import datetime, timezone


app = FastAPI()

transations = []

@app.get("/estatistica")
def search_transations():


@app.post("/transacao", status_code=201)
def transation_recept(transacao: TransationType):
    hora_atual = datetime.now(timezone.utc)
    if transacao.valor < 0:
        raise HTTPException(status_code=422, detail='Este valor não pode ser adicionado nas transações ')
    if transacao.dataHora > hora_atual:
        raise HTTPException(status_code=422, detail='Informação de data e hora errado')
    transations.append(transacao)

@app.delete("/transacao", status_code=200)
def delete_transations():
    transations.clear()
