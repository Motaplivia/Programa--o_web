# **Sistema de Biblioteca API** 📚

Este é um sistema simples desenvolvido com **FastAPI** que oferece operações CRUD para gerenciar Livros, Categorias e Empréstimos em uma biblioteca. O backend utiliza FastAPI, SQLite como banco de dados, e SQLAlchemy para ORM.

---

## **Tecnologias Utilizadas**

- **Python 3.7+**
- **FastAPI**: Framework para criação de APIs rápidas e eficientes.
- **SQLAlchemy**: ORM para gerenciar interações com o banco de dados.
- **SQLite**: Banco de dados leve para persistência de dados.

---

## **Pré-requisitos**

1. **Python 3.7+** instalado.
2. Gerenciador de pacotes `pip`.

---

## **Instalação**

1. **Clone o repositório:**

   ```bash
   git clone <url-do-repositorio>
   cd <nome-do-diretorio>
   ```

2. **Crie e ative um ambiente virtual:**

   No Linux/macOS:

   ```bash
   python3 -m venv venv
   source venv/bin/activate
   ```

   No Windows:

   ```cmd
   python -m venv venv
   venv\Scripts\activate
   ```

3. **Instale as dependências:**

   ```bash
   pip install -r requirements.txt
   ```

4. **Crie o banco de dados SQLite:**
   O banco de dados será criado automaticamente ao executar o código, com base nos modelos definidos.

---

## **Executando a API**

1. Crie o arquivo .env com as seguintes variáveis e introduza as informações:

   ```bash
   DATABASE_PORT=
   POSTGRES_PASSWORD=
   POSTGRES_USER=
   POSTGRES_DB=fastapi
   POSTGRES_HOST=
   POSTGRES_HOSTNAME=
   ```

2. Inicie o servidor:

   ```bash
   uvicorn main:app --reload
   ```

3. Acesse a documentação interativa no navegador:
   - Swagger UI: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)
   - Redoc: [http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

---

## **Endpoints**

### Livros 📖

- **GET /livros**: Lista todos os livros.
- **POST /livros**: Cria um novo livro.
- **PUT /livros/{livro_id}**: Atualiza um livro existente.
- **DELETE /livros/{livro_id}**: Deleta um livro.

### Categorias 📚

- **GET /categorias**: Lista todas as categorias.
- **POST /categorias**: Cria uma nova categoria.
- **PUT /categorias/{categoria_id}**: Atualiza uma categoria existente.
- **DELETE /categorias/{categoria_id}**: Deleta uma categoria.

### Empréstimos 🔑

- **GET /emprestimos**: Lista todos os empréstimos.
- **POST /emprestimos**: Realiza um novo empréstimo.
- **PUT /emprestimos/{emprestimo_id}**: Atualiza um empréstimo existente.
- **DELETE /emprestimos/{emprestimo_id}**: Deleta um empréstimo.

---

## **Modelos de Dados**

### Livro

- **titulo**: String
- **autor**: String
- **isbn**: String
- **categoria_id**: Inteiro (referência a `Categoria`)

### Categoria

- **nome**: String

### Empréstimo

- **livro_id**: Inteiro (referência a `Livro`)
- **aluno**: String
- **data_emprestimo**: String
- **data_devolucao**: String

---

### **Requisições**

- Para testar as requisições do projeto utilize o **Postman** e abra o arquivo **Biblioteca.postman_collection.json**.
