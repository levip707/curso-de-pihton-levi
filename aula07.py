# Lista de dicionários
listaPousts = [
    {
        "nome":"Maria",
        "descricao":"Foto de hoje",
        "foto":"https://www.toureiffel.paris/sites/default/files/styles/400x700/public/2025-08/hp_400x700_fmichel.jpg",
        "qtdLike":50,
        "qtdComent":30,
        "qtdComp":10
    },{
        "nome":"João",
        "descricao":"Viagem",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":60,
        "qtdComent":10,
        "qtdComp":15
    },{
        "nome":"Levi",
        "descricao":"Viagem",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":60,
        "qtdComent":10,
        "qtdComp":15
    },{
        "nome":"Davi",
        "descricao":"Viagem",
        "foto":"https://res.cloudinary.com/hello-tickets/image/upload/ar_4:3,c_fill,f_auto,q_auto,w_800/v1645846690/wswmwx31v9kjggw45v3h.jpg",
        "qtdLike":60,
        "qtdComent":10,
        "qtdComp":15
    }
]

# listaNomes = ['Carlos','Jessica']

# pessoa = {'nome':'Letícia', 'idade':28}
# print(pessoa["idade"])
# print(listaNomes[1])
# print(listaPousts[0]["nome"])

# poust = {}

# poust['nome'] = input('Digite seu nome: ')
# poust['descricao'] = input('Digite a descrição: ')
# poust['foto'] = input('Digite a url da foto: ')
# poust['qtdLike'] = int(input('Digite a quantidad de like: '))
# poust['qtdComent'] = int(input('Digite a quantidad de comentários: '))
# poust['qtdComp'] = int(input('Digite a quantidade de compartilhamentos: '))

# listaPousts.append(poust)

#print(listaPousts)

# listaNumeros = [1,2,3,5,12,312,31325,5643,5756,234]


# for numero in listaNumeros:
#     print(f'Número: {numero}')

# print('Pessoas que postaram:')
# for poust in listaPousts:
#     if poust["qtdLike"] > 50:
#         print(f'Nome: {poust["nome"]}')
#         print(f'Foto: {poust["foto"]}')
#         print(f'----------------------------------')

# 1. Crie um programa que percorra uma lista de dicionários que represente as postagens em uma rede social e mostre o total de likes somando a quantidade dee likes de todas as postagens.

somaLikes = 0
for post in listaPousts:
    somaLikes = somaLikes + post['qtdLike']
print(f'Total de likes = {somaLikes}')

# 2. Crie um programa que percorra a lista de posts e mostre o nome a descrição e a foto apenas das postagens que tiverem mais que 20 comentários

for post in listaPousts:
    if post['qtdComent'] >20:
        print(f'Nome: {post['nome']}\ndescricao: {post['descricao']}\nFoto: {post['foto']}')

# 3. crie um programa que analise as postagens dos usuários e calcule o engajamento, que é a soma de comentários, curtidas e compartilhamento. Mostre depois o post com maior engajamento.  

for post in listaPousts:
    engajamento =post['qtdComent']+post['qtdLike']+post['qtdComp']
    post['engajamento'] = engajamento

maiorEngajamento = 0

for post in listaPousts:
    if post['engajamento'] > maiorEngajamento:
        maiorEngajamento = post['engajamento']

print(maiorEngajamento)

#função
def Mengajamento(listaPousts):

    for post in listaPousts:
        engajamento =post['qtdComent']+post['qtdLike']+post['qtdComp']
        post['engajamento'] = engajamento

Mengajamento = 0

for post in listaPousts:
        if post['engajamento'] > maiorEngajamento:
            maiorEngajamento = post['engajamento']

        (maiorEngajamento)   