Transactions API

API REST para gerenciamento de transações financeiras, desenvolvida em Python com FastAPI, como resolução do desafio de backend do Itaú Unibanco.

Sobre o desafio

O objetivo é construir uma API que recebe transações financeiras e calcula estatísticas sobre elas, seguindo regras específicas de validação e armazenamento em memória (sem uso de banco de dados).

Endpoints
POST /transacao

Recebe uma nova transação.

Corpo da requisição:

json
{
    "valor": 123.45,
    "dataHora": "2020-08-07T12:34:56.789-03:00"
}

Regras de validação:

valor deve ser maior ou igual a 0
dataHora não pode estar no futuro

Respostas:

201 Created — transação aceita e registrada
422 Unprocessable Entity — transação recusada (valor negativo ou data inválida)
400 Bad Request — corpo da requisição mal formado
DELETE /transacao

Remove todas as transações armazenadas.

Respostas:

200 OK — dados apagados com sucesso
GET /estatistica

Retorna estatísticas das transações ocorridas nos últimos 60 segundos.

Resposta (200 OK):

json
{
    "count": 10,
    "sum": 1234.56,
    "avg": 123.456,
    "min": 12.34,
    "max": 123.56
}

Se não houver transações nos últimos 60 segundos, todos os campos retornam 0.

Tech Stack
Python
FastAPI
Pydantic (validação de dados)
Rodando localmente
bash
# Criar e ativar ambiente virtual
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows

# Instalar dependências
pip install -r requirements.txt

# Rodar a aplicação
uvicorn main:app --reload

A API estará disponível em http://localhost:8000, com documentação interativa (Swagger) em http://localhost:8000/docs.

Estrutura do projeto
transactions-api/
├── main.py           # Rotas e lógica dos endpoints
├── models.py         # Modelos Pydantic (TransationType)
├── requirements.txt  # Dependências do projeto
└── README.md