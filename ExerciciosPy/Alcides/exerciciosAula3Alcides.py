
'''
Exercicio 1

h = float(input('valor da altura do tronco da pirâmide (h) >> '))
Bmenor = float(input('valor da base menor (Bmenor) >> '))
Bmaior = float(input('valor da base maior (Bmaior) >> '))
volume = h / 3 * (Bmaior**2 + Bmenor**2 + (Bmaior**2 * Bmenor**2)**0.5)
print(f'O valor do volume do tronco da pirâmede das medidas escolhidas é {volume}')

'''

'''
Exercicio 2

horas = int(input('Digite um numero de horas >> '))
H_em_Min =  60 * horas
print(f'{horas} Horas em minutos é igual a {H_em_Min} minutos')

'''

'''
Exercicio 3

valorPrestacao = float(input('Digite o valor da prestação >> '))
multa = float(input('Porcentagem de multa pelo atraso >> '))
qtdeDias = int(input('Quantidade de dias de atraso >> '))
prestacao = valorPrestacao + (valorPrestacao * (multa/100) * qtdeDias)
print(f'o valor da prestação era de {valorPrestacao}, devido ao atraso, foi aplicada uma multa de {multa}%, resultando no valor total de R${prestacao}')

'''

"""
Exercicio 4

import math

grau = int(input('Valor em graus de um angulo >> '))
radiano = math.radians(grau)
print(f'seno = {math.sin(radiano):.2f} cosseno = {math.cos(radiano):.2f} tangente = {math.tan(radiano):.2f}')

#poderia usar try-except por conta da tangente, mas como não foi explicitado no exercicio, deixei assim rs

"""


"""
Exercicio 5

numero = int(input('Numero >>'))
imparOUpar = numero % 2 == 0
print('true = par | false = impar')
print(f'o numero {numero} é {imparOUpar}')

#como nao estou usando condicionais, tentei procurar um jeito de mostrar explicitamente par ou impar no print. O jeito seria uma lista, mas ainda nn abordei isso nas aulas.
"""