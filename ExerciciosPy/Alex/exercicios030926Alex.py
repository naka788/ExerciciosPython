"""
Exercício 01
Uma empresa de transporte por aplicativo calcula o valor da corrida considerando a distância
percorrida e o horário. A tarifa básica é de R$ 5,00 mais R$ 2,50 por quilômetro. Durante o horário
de pico, das 7h às 9h ou das 17h às 19h, é aplicado um adicional de 20% sobre o valor total da
corrida.
Escreva um programa que receba a distância percorrida, em quilômetros, e a hora de início da
corrida. Calcule e apresente o valor final a ser pago com duas casas decimais.


dist = float(input('distancia em KM >> '))
hrInicio = float(input('horario de inicio >> (7.25)'))
tarifaBase = float(5.0 + (dist * 2.5))
valor_final = tarifaBase

if (hrInicio >= 7 and hrInicio <= 9) or (hrInicio >= 17 and hrInicio <= 19):
    valor_final = tarifaBase + (tarifaBase * 0.2)
    print(f'valor a pagar: R${(valor_final):.2f}')
else: 
    print(f'valor a pagar: R${(valor_final):.2f}')
"""

"""
Exercício 02
Um festival permite a entrada desacompanhada somente para pessoas com 18 anos ou mais.
Menores de idade podem entrar apenas quando acompanhados por um responsável.
Escreva um programa que receba a idade do visitante e pergunte se ele está acompanhado por
um responsável, utilizando S ou N . A seguir, apresente uma mensagem informando se a entrada
será permitida.

idade = int(input('qual sua idade? >> '))
if idade < 18:
    acomp = input('voce esta acompanhando de um responsável maior de idade? S ou N >>  ')
    if acomp == 'S' or acomp == 's':
        print('entrada de menor liberada')
    elif acomp == 'N' or acomp == 'n':
            print('entrada de menor negada')
else: 
    print('entrada liberada')
"""
"""
Exercício 03
Uma empresa classifica o consumo mensal de energia em três faixas. Até 100 kWh, o consumidor
paga R$ 0,70 por kWh. De 101 a 200 kWh, paga R$ 0,85 por kWh sobre todo o consumo. Acima
de 200 kWh, paga R$ 0,95 por kWh.
Escreva um programa que receba o consumo mensal em kWh, calcule e apresente o valor da
conta com duas casas decimais.


kwh = int(input('consumo mensal em kwh >> '))
if kwh <= 100:
    valor = float(0.7)
elif kwh >= 101 and kwh <= 200:
    valor = float(0.85)
else:
    valor = float(0.95)

print(f'{kwh*valor:.2f}')
"""

"""
Exercício 04
Uma instituição financeira avalia pedidos de financiamento em duas etapas. Primeiro, verifica se o
cliente possui renda mensal de pelo menos R$ 3.000,00. Caso atenda a esse requisito, o sistema
analisa o percentual da renda comprometida com outras dívidas. Se esse percentual for de até
30%, o financiamento pode ser aprovado. Caso contrário, deve ser recusado. Clientes com renda
inferior a R$ 3.000,00 são recusados sem passar pela segunda análise.
Escreva um programa que receba a renda mensal do cliente e o percentual da renda já
comprometida com outras dívidas. Apresente uma mensagem informando se o financiamento será
aprovado ou recusado. Caso seja recusado, apresente o motivo da recusa.


rendaMensal = float(input('renda mensal>> '))
if rendaMensal < float(3000.00):
    print('financiamento recusado. Motivo: renda insuficiente, minimo: R$3.000,00')
else:
    prc = int(input('percentual de renda comprometida>> '))
    if prc > int(30):
        print('financiamente recusado. Motivo: percentual de renda comprometida maior que 30%')
    else:
        print('financiamento aprovado')

"""