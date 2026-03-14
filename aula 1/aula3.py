
# print( (3 + 5) * 2)

#1. Escreva um programa em python que receba do teclado 4 notas e calcule a média aritimética dessas notas, mostrando na tela o resultado.

# n1 = float(input('Digite a primeira nota: '))
# n2 = float(input('Digite a segunda nota: '))
# n3 = float(input('Digite a terceira nota: '))
# n4 = float(input('Digite a quarta nota: '))

# media = (n1 + n2 + n3 + n4 )/4
# print(f'A média é {media:.2f}')

# 2. Escreva um programa em python que receba 3 notas e 3 pesos e calcule a média ponderada notas.

# n1 = float(input('digite a primeira nota: '))
# n2 = float(input('digite a segunda nota: '))
# n3 = float(input('digite a terceira nota: ')) 

# p1 = float(input('digite a primeira peso: '))
# p2 = float(input('digite a segundo peso: '))
# p3 = float(input('digite a terceiro peso: '))

# mediaPonderada = (n1 * p1 + n2 * p2 + n3 * p3)/( p1 + p2 + p3)
# print(f'Sua média é: {mediaPonderada}')

# if condição:
#  Bloco de código
# else:
#  Bloco de código

# x = 10
# y = 5

# if x > y:
#     print('x é maior que y')
# elif y > x:
#     print('y é maior que x')
# else:
#     print('y é maior ou igual a x')

# # verifique se a média é maior ou igual a 7 e print aprovado, se a média estiver entre 4 e 7 print na tela recuperação e se a média for menor que quatro print na tela reprovado.

# if media >= 7:
#     print('aprovado')
# elif media >= 4:
#     print('recuperação')
# else:
#     print('reprovado')

#Laços  de repetição

#for variavel in range (valor)  

for i in range (10):
    print(f'o valor de i é {i+1}')

for i in range (1,11):
    print(f'o valor de i é {i}')

for i in range (1,10,2):
     print(f'o valoe de i é {i}')

# 1. Faça um laço de repetição que print os números de 1 até 20.

for i in range (10):
    print(f'o valor de i é {i+1}')

# 2. Faça um programa que print na tela a mensagem "olá mundo 10 vezes".



# 3. Faça faça um laço de repetição que printe os números de 0 até 100 pulando de 2 em 2


# 4. faça um laço de repetição que ira rodar 5 vezes e a cada volta ele terá que usar um input para pedir um número, mas somente printe em tela os números maiores que 10



# while condição ->não sabe o número de repetição
# for -> quando vc sabe o número de repetição

i = 0
while i < 10:
    i = int(input("digite um valor maior que 9: "))

# loop infinito

while True:
    i = int(input('digiti um número maior que 9: '))
    if i >9:
        print('Obrigado por ter digitado um número maior que 9')
        break

# 1. Faça um laço while que mostre os números de 1 até 10

# 2. Faça um laço



