# 2.Peça ao usuário um número e verifique se ele é impar ou par.

# numero = int(input('digite um número: '))
# if numero %2 == 0:
#     print('O número é pár')
# else:
#     print('O número é impar')

# # 3. Peça ao úsuario 3 notas de um aluno, caucule a média e se a média for maior que 7, mostre aprovado se não mostre recuperação

# nota1 = float(input('digite a nota'))
# nota2 = float(input('digite a nota'))
# nota3 = float(input('digite a nota'))

# media = (nota1 + nota2 + nota3)/3

# if media >= 7:
#     print('aprovado')
# else:
#     print('recuperação')

# 4. Peça para um usuário digitar um número e print se ele for positivo.



# 5. Peça para o usuário digitar o preço de um produto e diga se ele é caro se custar mais de 100 reais e barato se custar menos que 100.


# 6.

# saldo = 1000

# opcao = int(input('1 - consultar saldo\n2 - sacar\n3 - Depositar\nResposta;'))

# if opcao == 1:
#     print(f'saldo atual = {saldo}')
# elif opcao == 2:
#     saque = float(input('quanto você deseja sacar?'))
#     if saque > saldo:
#         print('saldo insuficiente')
#     else:
#         saldo = saldo - saque
#         print(f'saldo realizado com sucesso!\nsaldo atual = {saldo}')
# elif opcao == 3:
#     deposito = float(input('quanto você deseja deposita?'))
#     saldo = saldo + deposito
#     print(f'depósito realizado com sucesso!!\nSaldo atual = {saldo}')
# else:
#     print('opção inválida') 
        
#1. 

# opcao =''

# while(opcao != 3):
#     opcao = int(input('cadastrar usuário\n2 - listar usuários\n3 - sair do sistema\n'))
#     if opcao == 1:
#         nome = input('digite o nome')
#         telefone = input('digite o seu numero')
#         print('cadastro realizado com sucesso')
#     elif opcao == 2:
#         print('Maria - 859888888\nJoão - 85766778899')
#     elif opcao == 3:
#         print('saindo...')
#     else:
#         print('opção invalida')

#2.

# saldo = 1000

# opcao =''

# while(opcao != 4):
#     opcao int(input('1 - Consultar saldo\n1 - 2 - Sacar dinheiro\n2 - 3 - Depositar dinheiro'))

# #3. 
# for i in ranger (3):
#     desejo = input(f'desejo {i+1}')

#4.

# valor = float(input('digite o valor da compra: '))

# nparcelas = int(input('digite o número de parcelas desejado: '))

# while not (nparcelas <= 12 and nparcelas > 0):
#     nparcelas = int(input('digite o número de parcelas desejado: '))

# # while (nparcelas > 12 or nparcelas <= 0):
# #     nparcelas = int(input('digite o número de parcelas desejado: '))

# valorParcela = valor/nparcelas

# for i in range(nparcelas):
#     print(f'parcela {i+1} = {valorParcela}')

# crie um programa que tenha o seguinte menu
 1 - adicionar produtos ao carrinho
 2 - listar os produtos
 3 - sair 

produtos = ['notbook','tablet','mouse']

opcao = ''
while (opcao != 3):
    opcao = int(input('1 - adicionar produtos ao carrinho\n2 - listar os produtos'))
    if opcao == 1:
        produto = input('nome do produto: ')
        produto.append(produto)
    elif opcao == 2:
        for produto in produtos:
            print(produto)
    elif opcao == 3:
        print('saindo...')

