# app/crud.py

from app.models import livros, categorias, emprestimos, id_counter_livro, id_counter_categoria, id_counter_emprestimo
from app.schemas import Livro, Categoria, Emprestimo
from datetime import date


# CRUD para Livros
def add_livro(livro: Livro):
    global id_counter_livro
    livro_dict = livro.dict()
    livro_dict['id'] = id_counter_livro
    id_counter_livro += 1
    livros.append(livro_dict)
    return livro_dict

def get_livros():
    return livros

def update_livro(livro_id: int, updated_livro: Livro):
    for livro in livros:
        if livro["id"] == livro_id:
            livro.update(updated_livro.dict())
            return livro
    return None

def delete_livro(livro_id: int):
    global livros
    livros = [l for l in livros if l["id"] != livro_id]
    return {"message": "Livro deletado com sucesso"}

# CRUD para Categorias
def add_categoria(categoria: Categoria):
    global id_counter_categoria
    categoria_dict = categoria.dict()
    categoria_dict['id'] = id_counter_categoria
    id_counter_categoria += 1
    categorias.append(categoria_dict)
    return categoria_dict

def get_categorias():
    return categorias

def update_categoria(categoria_id: int, updated_categoria: Categoria):
    for categoria in categorias:
        if categoria["id"] == categoria_id:
            categoria.update(updated_categoria.dict())
            return categoria
    return None

def delete_categoria(categoria_id: int):
    global categorias
    categorias = [c for c in categorias if c["id"] != categoria_id]
    return {"message": "Categoria deletada com sucesso"}

# CRUD para Empréstimos
def add_emprestimo(emprestimo: Emprestimo):
    global id_counter_emprestimo
    emprestimo_dict = emprestimo.dict()
    emprestimo_dict['id'] = id_counter_emprestimo
    id_counter_emprestimo += 1
    emprestimos.append(emprestimo_dict)
    return emprestimo_dict

def get_emprestimos():
    return emprestimos

def update_emprestimo(emprestimo_id: int, updated_emprestimo: Emprestimo):
    for emprestimo in emprestimos:
        if emprestimo["id"] == emprestimo_id:
            emprestimo.update(updated_emprestimo.dict())
            return emprestimo
    return None

def delete_emprestimo(emprestimo_id: int):
    global emprestimos
    emprestimos = [e for e in emprestimos if e["id"] != emprestimo_id]
    return {"message": "Empréstimo deletado com sucesso"}
