# app/routers/categorias.py

from fastapi import APIRouter, HTTPException
from app.crud import add_categoria, get_categorias, update_categoria, delete_categoria
from app.schemas import Categoria
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Categoria], tags=["Categorias"])
def get_categorias_route():
    return get_categorias()

@router.post("/", response_model=Categoria, tags=["Categorias"])
def add_categoria_route(categoria: Categoria):
    return add_categoria(categoria)

@router.put("/{categoria_id}", response_model=Categoria, tags=["Categorias"])
def update_categoria_route(categoria_id: int, updated_categoria: Categoria):
    categoria = update_categoria(categoria_id, updated_categoria)
    if categoria:
        return categoria
    raise HTTPException(status_code=404, detail="Categoria não encontrada")

@router.delete("/{categoria_id}", response_model=dict, tags=["Categorias"])
def delete_categoria_route(categoria_id: int):
    return delete_categoria(categoria_id)
