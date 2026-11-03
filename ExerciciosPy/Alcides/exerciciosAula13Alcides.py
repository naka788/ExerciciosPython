def cadastrarMulta(placa, valor):
    multas[placa] = valor
    return f'Uma multa no valor de {valor} foi atribuida a nova placa: {placa}'
def buscaMultaPlaca(placa, multas):
    return f'O valor referente a multa da placa {placa} é igual a R${multas.get(placa):;}'
def listaMulta(multas):
    pass
def placaMultaMaxMin(multas):
    pass
def calcMediaMultas(multas):
    pass

multas = {
'ABC1234': 150.50,
'DEF5678': 200.75,
'GHI9012': 180.25,
'JKL3456': 100.00,
'MNO7P89': 220.30,
'PQR1S23': 175.60,
'STU5T67': 190.45,
'VWX9U01': 210.20,
'YZA3V45': 160.75,
'BCD789F': 195.80
}

while True:
    menu = int(input('1 - Cadastrar multa (placa, valor)\n2 - Buscar multa pela placa\n3 - Listar todas as multas\n4 - Exibir placa/multa referente ao valor mais alto e mais baixo\n5 - Calcular o valor médio de todas as multas\n6 - Sair\nQual opção você quer: '))
    if menu < 1 or menu > 6:
        print('Insira opção válida!!!\n')
    elif menu == 1:
        placa = str(input('Qual a placa do carro: '))
        valor = float(input('Qual o valor da multa: '))
        print(cadastrarMulta(placa, valor))
        print(multas)
    elif menu == 2:
        placa = str(input('Qual a placa do carro: '))
        print(buscaMultaPlaca(placa, multas))
    """
    elif menu == 3:
        continue
    elif menu == 4:
        continue
    elif menu == 5:
        continue
    
    elif menu == 6:
        break
        """
    