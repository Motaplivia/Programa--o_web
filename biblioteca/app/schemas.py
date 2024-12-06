# app/schemas.py

from pydantic import BaseModel
from typing import Optional
from datetime import date

# Modelo para Livro
class Livro(BaseModel):
    titulo: str
    autor: str
    isbn: str
    categoria_id: int

# Modelo para Categoria
class Categoria(BaseModel):
    nome: str

# Modelo para Emprestimo
class Emprestimo(BaseModel):
    livro_id: int
    aluno: str
    data_emprestimo: date
    data_devolucao: Optional[date] = None
