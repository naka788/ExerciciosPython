"""
Escreva um programa em Python que leia um grupo de valores inteiros e determine quantos valores são
positivos e quantos são negativos. Determine, também, qual é o menor desses valores. Para encerrar a leitura,
digite 0.
"""
num = int()
menorNum = 0
contadorPositivo = 0
contadorNegativo = 0

while True:
    num = int(input('digite um numero inteiro: '))
    if num == 0:
        break
    elif num > 0:
        contadorPositivo += 1
    else:
        contadorNegativo += 1
    if num < menorNum:
        menorNum = num

print(f'Você digitou {contadorPositivo} numeros positivos e {contadorNegativo} numeros negativos!')
print(f'O menor valor digitado foi {menorNum}')