"""
1- Faça uma função que receba como parâmetros o Km inicial, Km final, quantidade
de litros gastos e preço do litro. Calcule e mostre:
- Distância percorrida;
- Consumo médio;
- Valor gasto;
Faça um programa principal que solicite para o usuário o valor da quilometragem
inicial, final, a quantidade de litros gastos e o preço do litro e mostre a distância
percorrida, o consumo médio e o valor gasto, para isso utilize a função definida
acima.

def dadosViagem(km1,km2,litroGasto,precoLitro):
    distPerc = km2 - km1
    consuMed = distPerc / litroGasto
    valorGasto =  litroGasto * precoLitro
    return distPerc, consuMed, valorGasto


a = float(input('km inicial>> '))
b = float(input('km final>> '))
c = float(input('qnt litros gastos>> '))
d = float(input('preço litro>> '))

distPerc, consuMed, valorGasto = dadosViagem(a,b,c,d)

print(f'distancia percorrida: {distPerc:.2f}Km')
print(f'Consumo medio: {consuMed:.2f} Km/L')
print(f'Valor total gasto: R${valorGasto:.2f}')
"""

"""
2- Construir uma função que receba como parâmetros o valor de uma compra e a
quantidade de parcelas e calcula e retorna o valor da parcela, sabendo que a loja
acrescenta 5% de juros para as compras parceladas.
No algoritmo principal, solicite para o usuário o valor de uma compra e a quantidade
de parcelas e utilizando a função descrita acima, mostre o valor da parcela


def compraParcelada(valorCompra,qntParcelas):
    valorParcela = (valorCompra / qntParcelas) * 1.05
    return valorParcela

valorCompra = float(input('valor da compra>> R$'))
qntParcelas= int(input('quantidade de parcelas (caso não queira parcelas, digite 1)>> '))
if qntParcelas > 1:
    print(f'o valor total da compra parcelada: R${(compraParcelada(valorCompra,qntParcelas) * qntParcelas):.2f}')
    print(f'valor das parcelas: R${compraParcelada(valorCompra,qntParcelas):.2f}')
    print(f'quantidade de parcelas: {qntParcelas}')
else:
    print(f'valor total da compra: R${valorCompra}')

"""