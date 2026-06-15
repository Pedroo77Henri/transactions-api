from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def search_transations():
    return {'status':'ok'}
