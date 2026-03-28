#  #aula 05 - Revisão de lista
# # maneira errada
# nome1 = 'Maria'
# nome2 = 'João'

# #maneira certa    0       1      2
# listaDeNomes = ['Maria','João','Pedro']

# print(listaDeNomes [0])

# listaDeNomes[1]= 'Tiago'
 
# for nome in listaDeNomes:
#     print(nome)

# # Crie uma lista com 10 números e use o for para printar na tela cada um dos 10 números

# listaNumeros = [1,2,3,4,5,6,7,8,9,10]

# for numeros in listaNumeros:
#     print(numeros)

# # A partir da primera lista, use um for para percorrer a lista e printar os números maiores que 5.

# for numeros in listaNumeros:
#     if numeros > 5:
#         print(numeros)

# Funções internas de listas

# append() -> Acrescenta no final de uma lista
# insert(0,item)-> Acrescenta em uma posição
# pop() -> Deleta o ultimo item da lista
# pop(0) -> Deleta umaposição da lista
# del(lista[x:y])-> deleta um intervalo de uma lista

#1. Crie uma lista vazia chamada aprovados. peça para o usuário digitar 5 notas, e para cada nota:
# Se a nota for maior ou igual a 7. Adicione na lista aprovados caso contrário, ignore

# aprovados = []

# for i in range(5):
#     notas = float(input('digite uma nota :'))
#     if notas >= 7:
#         aprovados.append(notas)

# print(aprovados)

#2. Dada a lista:res = [5, 12, 20, 3, 15] percorra alista e remova os números menores que 10. Mostre a lista com o resultado final

# valores = [5, 12, 7, 15, 3, 20]
# valoresMaiores = []

# for valor in valores:
#     if valor >= 10:
#         valoresMaiores.append(valor)

# valores = valoresMaiores

# print(valores)

# Dicionário

from re import L


pessoa = {
    'nome':'maria',
    'idade':20,
    'cidade':'Fortaleza'
}
print(pessoa)
print(pessoa['nome'])

# Crie um dicionário chamado aluno e salve o nome, o curso e a média desse aluno recebendo esses dados do teclado(usando o input).

nome = input('digite o nome do aluno :')

curso = input('digite o curso do aluno :')

media = int (input('digite a média do aluno :'))

aluno = {
    'nome':nome,
    'curso':curso,
    'media': media
}
print(aluno)

print(f'Olá {aluno['nome']} seja bem vindo ao cruso de{aluno[curso]}')