from fastapi import FastAPI
from models import TransationType
from fastapi import HTTPException
from datetime import datetime, timezone, timedelta


app = FastAPI()

transations = []

@app.get("/estatistica")
def search_transations():
    time_limit = datetime.now(timezone.utc) - timedelta(seconds=60)
    recents_transations = [item for item in transations if item.dataHora >= time_limit]
    valores = [transacao.valor for transacao in recents_transations]
    if not valores:
        return{
            "count": 0,
            "max": 0,
            "min": 0,
            "sum": 0,
            "avg": 0,
        }
      
    else:
        quantidade = len(valores)
        maximo = max(valores)
        minimo = min(valores)
        total = sum(valores)
        media = total  / quantidade
        return {
                "count": quantidade,
                "max": maximo,
                "min": minimo,
                "sum": total,
                "avg": media
                }



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
