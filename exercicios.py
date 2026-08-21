"""
Exercicio 1 | comissao + salario
salario = float(input('Qual o seu salario? (Formato: xxxxxxx.xx)'))
comissao = salario * 0.05
print (f'Seu salario de {salario} ganhou uma comissão no valor de {comissao:.2f}, totalizando {(salario + comissao):.2f}')

"""
"""
exercicio 2 | calculo de velocidade media em km/h

distanciaCD = float(input('Qual a distancia em KM entre as duas cidades? '))
horasViagem = int(input('Quantas horas leva para percorrer de uma cidade a outra? '))
minutosViagem = int(input('E minutos? '))
tempoViagem = horasViagem  + (minutosViagem / 60)
velocidadeMed = distanciaCD / tempoViagem
print(f'a velocidade média é {velocidadeMed:.2f}km/h')

"""
"""
exercicio 3 | conversor dolar para real

cotDolarReal = float(5.1949)
dolar = float(input('$ '))
print(f'{(dolar * cotDolarReal):.2f}')

"""

"""
exercicio 4 | gasto restaurante + 10% do garçom

valorGasto = float(input('Quanto o cliente gastou? R$'))
gorjetaGarçom = valorGasto * float(0.1)
valorTotal = valorGasto + gorjetaGarçom
print(f'O valor total a se pagar, considerando a taxa do garçom, é de R${valorTotal:.2f}')

"""