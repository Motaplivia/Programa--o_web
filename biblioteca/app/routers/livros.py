# app/routers/livros.py

from fastapi import APIRouter, HTTPException
from app.crud import add_livro, get_livros, update_livro, delete_livro
from app.schemas import Livro
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Livro], tags=["Livros"])
def get_livros_route():
    return get_livros()

@router.post("/", response_model=Livro, tags=["Livros"])
def add_livro_route(livro: Livro):
    return add_livro(livro)

@router.put("/{livro_id}", response_model=Livro, tags=["Livros"])
def update_livro_route(livro_id: int, updated_livro: Livro):
    livro = update_livro(livro_id, updated_livro)
    if livro:
        return livro
    raise HTTPException(status_code=404, detail="Livro não encontrado")

@router.delete("/{livro_id}", response_model=dict, tags=["Livros"])
def delete_livro_route(livro_id: int):
    return delete_livro(livro_id)
