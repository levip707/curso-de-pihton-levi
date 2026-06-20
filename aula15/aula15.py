# Se clonar o repositório usar esses comandos:
# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install -r requirements.txt - instala as dependências do projeto

# pip install supabase
# pip install python-dotenv
# pip install fastapi - para criar a API
# pip install uvicorn - para rodar a API

# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env

# Executar o fastapi com o uvicorn
# uvicorn aula15:app --reload -> para rodar a API

import os
from dotenv import load_dotenv
from supabase import create_client #
from fastapi import FastAPI
import requests

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #
# CRUD

app = FastAPI()

# selecao = input('Digite o produto que deseja buscar: ')
# produtos = requests.get(f'https://fakestoreapi.com/products/{selecao}').json()

# print(produtos['image'])

# Criação das primeiras rotas da API

@app.get('/livros')
def get_livros():
    resposta = supabase.table('biblioteca_livro').select('*').execute()
    livros = resposta.data
    return livros

@app.get('/livros/{id}')
def get_livros_id(id: int):
    resposta = supabase.table('biblioteca_livro').select('*').eq('id',id).execute()

    livros = resposta.data

    if len(livros) == 0:
        return {"Mensagem: Livro não encontrado"}

    return livros

# Query strings
# www.google.com/

@app.get('/busca')
def busca(titulo: str, quantidade: int, genero: str, ano: int):
    elementosBusca = {
        'titulo': titulo,
        'quantidade': quantidade,
        'genero': genero,
        'ano': ano
    }
    resposta = supabase.table('biblioteca_livro').select('*').ilike('titulo',f'%{titulo}%').execute()
    return elementosBusca

# @app.get('/busca')
# def busca(titulo: str = None, quantidade: int = None, genero: str = None, ano: int = None):
#     reposta = supabase.table('biblioteca_livro').select('*')
#     if titulo:
#         resposta = reposta.ilike('titulo', f'%{titulo}%')
#     if quantidade:


# Post

from fastapi import Body

@app.post('/livros')
def cadastrar_livros(dados: dict = Body()):

    resposta = supabase.table('biblioteca_livros').ins ert(dados).execute()


    return {'msg':'Cadastro de livros'}

# update /put

@app.put('/atualizaelivro/{id}')
def atualizarlivro(id:int, dados: dict = Body())

    reposta = supabase.table('biblioteca_livro').update(dados).eq('id',id).execute()

    return {
        'msg': 'Livro atualizado',
        'dados':resposta.data
    }