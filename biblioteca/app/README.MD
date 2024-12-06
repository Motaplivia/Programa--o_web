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
<<<<<<< HEAD

### Passo 2: Criar e Ativar o Ambiente Virtual 🧑‍💻
Crie um ambiente virtual para o projeto e ative-o:

```bash
python -m venv venv  # Criação do ambiente virtual

# Ativar o ambiente virtual:
# Windows:
.\venv\Scripts\activate

### Passo 3: Instalar Dependências 📦
Instale as dependências necessárias com o pip:

```bash
pip install -r requirements.txt


# Linux/macOS:
source venv/bin/activate

### Passo 4: Rodar o Servidor ⚡
Inicie o servidor com o Uvicorn:

```bash
uvicorn app.main:app --reload

### Passo 5: Documentação Interativa 📑
Acesse a documentação interativa da API gerada automaticamente pelo FastAPI no seguinte link:

[http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

O FastAPI gera automaticamente uma documentação interativa e fácil de usar, onde você pode testar diretamente as rotas da API. Essa documentação ajuda a entender como interagir com os endpoints da API sem a necessidade de outras ferramentas.

Além disso, também está disponível uma versão alternativa da documentação, mais voltada para a especificação da API, no seguinte link:

[http://127.0.0.1:8000/redoc](http://127.0.0.1:8000/redoc)

### Testando a API no Postman 📬
A API foi documentada usando o Postman. Para importar a coleção de testes, siga os passos abaixo:

1. Abra o Postman.
2. Importe a coleção de testes fornecida:
   - Clique em **File** > **Import**.
3. Selecione o arquivo da **Postman Collection** exportado ou baixe o arquivo da coleção se estiver fornecido no repositório.
4. Teste as rotas usando as requisições pré-configuradas no Postman.

Isso permitirá que você interaja com a API de maneira prática, testando as rotas de acordo com os exemplos fornecidos.

### Exemplos de Rotas 🌐

Aqui estão alguns exemplos de rotas que você pode testar na API:

---

#### Livros 📖

- **GET /livros**: Retorna todos os livros cadastrados.

    **Exemplo de Requisição**:
    ```bash
    Método: GET
    URL: http://127.0.0.1:8000/livros
    ```

- **POST /livros**: Cria um novo livro.

    **Exemplo de Requisição**:
    ```bash
    Método: POST
    URL: http://127.0.0.1:8000/livros
    Corpo:
    {
        "titulo": "O Senhor dos Anéis",
        "autor": "J.R.R. Tolkien",
        "isbn": "978-0261102385",
        "categoria_id": 1
    }
    ```

---

#### Categorias 📚

- **GET /categorias**: Retorna todas as categorias cadastradas.

    **Exemplo de Requisição**:
    ```bash
    Método: GET
    URL: http://127.0.0.1:8000/categorias
    ```

- **POST /categorias**: Cria uma nova categoria.

    **Exemplo de Requisição**:
    ```bash
    Método: POST
    URL: http://127.0.0.1:8000/categorias
    Corpo:
    {
        "nome": "Ficção"
    }
    ```

---

#### Empréstimos 🔑

- **GET /emprestimos**: Retorna todos os empréstimos cadastrados.

    **Exemplo de Requisição**:
    ```bash
    Método: GET
    URL: http://127.0.0.1:8000/emprestimos
    ```

- **POST /emprestimos**: Realiza um novo empréstimo.

    **Exemplo de Requisição**:
    ```bash
    Método: POST
    URL: http://127.0.0.1:8000/emprestimos
    Corpo:
    {
        "livro_id": 1,
        "aluno": "João Silva",
        "data_emprestimo": "2024-12-01",
        "data_devolucao": null
    }
    ```

### Como Contribuir 🤝

1. Fork o repositório para o seu GitHub.
2. Crie um branch para a sua feature:
    ```bash
    git checkout -b minha-feature
    ```
3. Faça suas alterações, commit e push:
    ```bash
    git add .
    git commit -m "Descrição da minha feature"
    git push origin minha-feature
    ```
4. Abra um **Pull Request** no repositório principal.

---


### Agradecimentos 🙏

Agradecemos pela contribuição! Se você tiver mais perguntas ou sugestões de melhorias, sinta-se à vontade para abrir um **issue** ou enviar um **pull request**.


=======
>>>>>>> ad6925302739d6b257ea62d39e79164dae3a9bb1
