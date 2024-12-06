# **Sistema de Biblioteca API** 📚

## **Descrição** 📝

O **Sistema de Biblioteca API** é uma aplicação web desenvolvida com **FastAPI** para gerenciar livros, categorias e empréstimos em uma biblioteca. A API oferece operações para realizar o cadastro, atualização, exclusão e consulta de livros, categorias e empréstimos, além de permitir consultar quais livros estão disponíveis em determinada categoria.

### **Problema que resolve** 💡

Este sistema foi desenvolvido para resolver o problema de gerenciamento de livros e empréstimos em bibliotecas. Ele permite que bibliotecas mantenham o controle sobre os livros disponíveis, as categorias de livros e os empréstimos realizados pelos alunos. O sistema facilita a consulta e atualização de dados, além de garantir que os livros não sejam emprestados mais de uma vez simultaneamente.

---

## **Funcionalidades** ⚙️

- **📖 Gerenciamento de Livros**:
  - Cadastro de livros com título, autor, ISBN e categoria.
  - Atualização e exclusão de livros.
  - Consulta de todos os livros cadastrados.

- **📚 Gerenciamento de Categorias**:
  - Cadastro de categorias de livros.
  - Atualização e exclusão de categorias.
  - Consulta de todas as categorias cadastradas.

- **🔑 Empréstimos**:
  - Realização de empréstimos de livros para alunos.
  - Consulta de todos os empréstimos realizados.
  - Atualização de empréstimos (como data de devolução).
  - Exclusão de empréstimos.

- **🔍 Consultas**:
  - Consulta dos livros disponíveis em uma determinada categoria.

---

## **Requisitos Técnicos** 🛠️

- **Python 3.7+**: A aplicação foi desenvolvida utilizando Python 3.7 ou superior.
- **FastAPI**: Framework para construção de APIs.
- **Uvicorn**: Servidor ASGI para rodar a aplicação.
- **Pydantic**: Para validação e serialização dos dados.
- **Postman**: Para testes da API.

---

## **Instalação e Execução** 🚀

### **Passo 1: Clonar o Repositório** 🔄

Clone o repositório para o seu computador:

```bash
git clone https://github.com/seu-usuario/biblioteca-api.git
cd biblioteca-api
