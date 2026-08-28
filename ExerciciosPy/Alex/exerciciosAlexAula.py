'''
Exercicio 3

tempoSeg = int(input('Segundos:'))
horas = tempoSeg // 3600
minutos = (tempoSeg % 3600) // 60
segundos = (tempoSeg % 3600) % 60
print(f'{horas}H:{minutos}M:{segundos}S') 

'''
'''
Exericio 4

cotMoedaEstrangeira = float(input('Qual a cotação da moeda estrangeira em relação a moeda local? '))
QntMoedaEstrangeira = float(input('Quanto dessa moeda estrangeira sera convertido para a moeda local? '))
conversão = QntMoedaEstrangeira * cotMoedaEstrangeira
print(f'{(QntMoedaEstrangeira):.2f} é equivalente a {(conversão):.2f}')

'''

'''
Exercicio 5

custoFabricaSemTax = float(input('custo fabrica >> '))
custoFabricaComTax = custoFabricaSemTax + (custoFabricaSemTax * 0.28)
impostos = custoFabricaComTax * 0.45
custoConsumidor = custoFabricaComTax + impostos
print(f'Custo total: {(custoConsumidor):.2f}')

'''
