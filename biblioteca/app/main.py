# app/main.py

from fastapi import FastAPI
from app.routers import livros, categorias, emprestimos

app = FastAPI()

app.include_router(livros.router, prefix="/livros", tags=["Livros"])
app.include_router(categorias.router, prefix="/categorias", tags=["Categorias"])
app.include_router(emprestimos.router, prefix="/emprestimos", tags=["Empréstimos"])

@app.get("/", tags=["Root"])
def read_root():
    return {"message": "Bem-vindo à API de Gerenciamento de Biblioteca!"}
