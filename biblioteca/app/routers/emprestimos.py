# app/routers/emprestimos.py

from fastapi import APIRouter, HTTPException
from app.crud import add_emprestimo, get_emprestimos, update_emprestimo, delete_emprestimo
from app.schemas import Emprestimo
from typing import List

router = APIRouter()

@router.get("/", response_model=List[Emprestimo], tags=["Empréstimos"])
def get_emprestimos_route():
    return get_emprestimos()

@router.post("/", response_model=Emprestimo, tags=["Empréstimos"])
def add_emprestimo_route(emprestimo: Emprestimo):
    return add_emprestimo(emprestimo)

@router.put("/{emprestimo_id}", response_model=Emprestimo, tags=["Empréstimos"])
def update_emprestimo_route(emprestimo_id: int, updated_emprestimo: Emprestimo):
    emprestimo = update_emprestimo(emprestimo_id, updated_emprestimo)
    if emprestimo:
        return emprestimo
    raise HTTPException(status_code=404, detail="Empréstimo não encontrado")

@router.delete("/{emprestimo_id}", response_model=dict, tags=["Empréstimos"])
def delete_emprestimo_route(emprestimo_id: int):
    return delete_emprestimo(emprestimo_id)
