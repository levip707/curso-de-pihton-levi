from supabase import create_client

supabase = create_client('','')

# resposta = supabase.table('employee').select('*').execute()
# resposta = resposta.data
# print(resposta)

def mostrarResultado(listaResultados):
   for resultado in listaResultados:
        for key, value in resultado.items():
            print(f'{key}: {value}')
        print('-'*30)
# Quetões
# 1. Liste todos os funcionário mostrando apenas o firstname, lastname e emailaddress.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 2. Mostrar os 10 funcionários mais jovens da empresa, ordenando por idade.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress,idade').order('idade').limit(10).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 3. Liste apneas os funcionário que possuem vacationhours maior = 40.

# resposta = supabase.table('employee').select('firstname,lastname,emailaddress').eq('vacationhours',40).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

'''
.eq('coluna',valor) -> igual
.neq('coluna', valor) -> diferente (não igual)
.gt('coluna',valor) -> Maior que
.gte('coluna',valor) -> Maior ou igual
.lt('coluna',valor) -> Menor que
.lte('coluna',valor) -> Menor ou igual
.like('coluna','%texto%') -> link '%texto%'
.in_('coluna',[1,2,3,...valores]) -> se esses valores constam na coluna

'''

# 4. Mostre firstname, emailaddress e departmentname dos funcionários do departamento Production.

resposta = supabase.table('employee').select('firstname,emailaddress,departmentname').eq('departmentname','Production').execute()
resposta = resposta.data
mostrarResultado(resposta)

# 5. Liste os funcionários cujo firstname começa com a letra A.

# resposta = supabase.table('employee').select('firstname,emailaddress').like('firstname','A%').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 6. Mostre os funcionários que possuem idade entre 30 e 50 anos.

# resposta = supabase.table('employee').select('firstname','idade').gt('idade',30).lt('idade',65).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 7. Liste firstname, idade e baserate dos funcionários com salário (baserate) maior que 60.

# resposta = supabase.table('employee').select('firstname','idade','baserate').gt('baserate',60).execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 8. Mostre os funcionários cujo emailaddress contém gmail.

# resposta = supabase.table('employee').select('emailaddress').like('emailaddress','%gmail%').execute()
# resposta = resposta.data
# mostrarResultado(resposta)

# 9. Liste apenas os funcionários com currentflag = true.
# 10. Mostre os funcionários do gênero masculino (gender = 'M') ordenados da maior para a menor idade.

'''
C -> CREAT - INSERIR DADOS - INSERT
R -> READ - LEITURA DE DADOS - SELECT
U -> UPDATE - ATUALIZAÇÃO DE DADOS - UPDATE
D -> DELETE - APAGAR ALGUM DADO - DELETE

'''

# usuario = {
# 'nome':'João',
# 'email':'joao@gmail.com',
# 'idade':29,
# 'senha':'senha123'
# }
# try:
#     resposta = supabase.table('usuarios').insert(usuario).execute()
#     print(resposta.data)
# except Exception as e:
#     print(e.message)

# usuario ={
# 'nome':'Maria Clara',
# 'idade':20
# }

# resposta = supabase.table('usuarios').update(usuario).eq('id',1).execute()
# print(resposta.data)

# resposta = supabase.table('usuario').delete().eq('id',6).execute()
# print(resposta.data)


#1 - Crie uma tabela chamada produtos no supabase que deve ter:
#id
#nome
#preço
#quatidade
#criado_em
#descricao

#2 - Insira manualmente 3 produtos diretamente pelo supa base.

#3 - Crie uma função para mostrar o nome o preço e a descrição dos produtos com o preço maior que 100 reais

def mostrarProdutos():
    resposta = supabase.table('produtos').select('nome, preco, descricao').gt('preco',100).execute()
    resposta = resposta.data
    return resposta

print(mostrarProdutos())


#4 - Crie uma função que receba como parâmetros o nome, preço, quantidade e descrição, e faça o cadastro de um novo produto no banco de dados


def cadastrarProduto(nome,preco,quantidade,descricao):

    produto = {
    'nome':nome,
    'preco':preco,
    'quantidade':quantidade,
    'descricao':descricao
    }
    try:
        resposta = supabase.table('produtos').insert(produto).execute()
        print(resposta.data)
    except Exception as e:
     print(e.message)

# cadastrarProduto('notbook',2000,10,'notbook acer')


#5 - Crie uma função que receba como parâmetro o ID e o novo preço de um produto, e a função deve atualizar o preço desse produto

produto ={

    'id':id,
    'preco':preco
}


#6 - Crie uma função que receba o ID de um produto e delete ele do banco de dados

# Utilize as funções criadas anteriormente para fazer um menu de opções com o while, fazendo:
#Opção 1: Cadastrar um novo Produto
#OPção 2: Listar os produtos e o prço
#OPção 3: Atualizar o preço e o produto
#Opção 4: Deletar um produto
#Opção 5: sair
# lembre-se que para cadastrar é nescessario que o usúario forneça os dados(nome, prço e descrição...), para atualizar o usúario precisa fornercer o ID e o novo preço e para deletar o usúario precisa fornecer o id.