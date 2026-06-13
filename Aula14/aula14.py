# python -m venv venv - cria o ambiente virtual
# venv/scripts/activate - ativa o ambiente virtual
# pip install supabase
# pip install python-dotenv
# criar o arquivo requirements.txt
# pip freeze > requirements.txt - salva as dependências do projeto no arquivo requirements.txt
# criar o arquivo .env
# criar o arquivo .gitignore -> venv e .env

#executar o fastapi com o uvicorn
# uvicorn aula14:app --reload

from dotenv import load_dotenv
from supabase import create_client #
from fastapi import FastAPI
import requests
import os

load_dotenv()

supabase_url = os.getenv('SUPABASE_URL')
supabase_key = os.getenv('SUPABASE_KEY')
supabase = create_client(supabase_url,supabase_key) #
# CRUD

app = FastAPI()

#selecao = input('digite o id do produto: ')
#produto = requests.get(f'https://fakestoreapi.com/products/{selecao}').json()

#print(produto)

#cep = input('digite o seu cep: ')
#endereco = requests.get(f'https://viacep.com.br/ws/{cep}/json/').json()

#print(endereco)

# criação das primeiras rotas da api
@app.get('/livros')
def get_livros():
    resposta = subase.table ('biblioteca_livro').select('*').execute()
    livro = resposta.data
    return livro

@app.get('/livros/{id}')
def get_livros_id(id: int):
    resposta = subase.table ('biblioteca_livro').select('*').eq('id'id).execute()
    livros = resposta.data
    return livros 
