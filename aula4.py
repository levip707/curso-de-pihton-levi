# #definição de uma lista em python

# # listaDeNomes = ['dionizio','Davi','Letícia','Jéssica',10,100,1000]

# # print(listaDeNomes[3]) #Quarto elemento da lista
# # print(listaDeNomes[0]) #primeiro elemento da lista
# # print(listaDeNomes[-1]) #últimoelemento da lista
# # print(listaDeNomes[-2]) #penúltimo elemento da lista

# # listaDeNomes[3] = 'Jéssica'

# # print(listaDeNomes)

# #questão 1
# from xml.etree.ElementInclude import LimitedRecursiveIncludeError


# listaNomes = ['ferro','cobre','prata','ouro','diamante']

# print(listaNomes[0])

# #questão 2
# listaNumeros = [10,100,1000,10000,100000,1000000]

# print(listaNumeros[0] + listaNumeros[-1])

# #questão 3
# listaElementos = ['ar','água','terra','plantas','minérios']

# listaElementos[3] = 'animais'
# print(listaElementos)

# #Fatiamento de lista
# #                 0 1 2 3 4 5 6 7 8 9 10
# # listaDeNumeros = [3,4,5,6,7,8,9,10,11,12]

# # print(listaDeNumeros)

# # listaDeNumeros2 = listaDeNumeros[0:7:2]

# # print(listaDeNumeros2)

# # listaNomes = ['joão','Maria','pedro','Tiago','carla','jessica']

# # listaCompleta = listaDeNumeros + listaDeNumeros2

# # print(listaCompleta)

# # print(listaNomes * 3)

# # print(listaNomes[2:5])

# #1. Crie uma lista de 0 até 5 e outra lista de 6 até 10, depois some as duas

# numerosParte1 = [0,1,2,3,4,5]
# numerosParte2 = [6,7,8,9,10]

# numeroscompletos = numerosParte1 + numerosParte2 

# print(numeroscompletos)

# #2. Crie uma lista com 5 valores númericos ec some os três últimos itens da lista.

# numeros = [0,1,2,3,4,5,6,7,8,9,10]

# soma = numeros[-1] + numeros[-2] + numeros[-3]

# #3. Crie uma lista com 5 valores e multiplique ela por 2

# numerosDobrados = numeros * 2

# print(numerosDobrados)

# #listaNomes = ['joão','Maria','pedro','Tiago','carla','jessica']
# #listaNomes[3] ='caio'
# flagAchou = False

# for nome in listaNomes:
#     if 'Caio'== nome:
#         print('o caio faz parte da lista')
#         flagAchou = True
#         break 

# if flagAchou == False:
#     print('o caio não faz parte da lista')
#  #1. Faça uma lista com 10 números depois percorra cada elemento com um laço de repetição e mostre cada um deles na tela

# listaNumeros10 = [10,20,30,40,50,60,70,80,90,100]

# for numero in listaNumeros10:
#     print(numero)

#  #2. Faça uma lista com 10 números e depois percorra cada elemento com um laço de repetição, porém exiba somente os números pares. 

# listaNumeros100 = [10,21,30,41,50,60,70,80,90,100]

# for numero in listaNumeros100:
#     if numero % 2 == 0:
#         print(f'O número {numero} é par')

# # ....

# listaNomes.append('David') #Adiciona um elelmento no final da lista
# #listaNomes.apdend(10)

# listaNomes.insert(0,'Aline') #Adiciona um elemento em uma posição da lista
# listaNomes.insert(3,'Gabriel')
# print(listaNomes)

# listaNomes.pop() #Remove um elemento do final da lista
# listaNomes.pop(0) #Remove um elemento de uma posição da lista
# print(listaNomes)

# del(listaNomes[2:5])
# print(listaNomes)

# #1. Faça uma lista de nome inicialmente vazia e após isso, crei um for para adicionar 5 nomes dentro dessas lista vindos do input.

# listaDeNomesVazia = []
# for i in range(5):
#     nome = input('digite um nomes:')
#     listaDeNomesVazia.append(nome)
#     print(listaDeNomesVazia)

#2. Crie uma lista com 5 elementos e remova os últimos 3 elementos de dentro dela ultilizando um for.

listaElementoss = ['arroz','feijão','farinha','carne','peixe']
for i in range(3):
    listaElementoss.pop()
    print(listaElementoss)
    
#3. Crie uma lista com 10 nomes. Solicite que o usuário digite um nome. digitado faz parte da lista. "usuário encontrado" se não, "usuário não encontrado"
