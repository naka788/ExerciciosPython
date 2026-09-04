"""
exercicio 1


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


