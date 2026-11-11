def cadastrarMulta(placa, valor):
    multas[placa] = valor
    return f'Uma multa no valor de {valor} foi atribuida a nova placa: {placa}'

def buscaMultaPlaca(placa, multas):
    busca = f'A placa não existe no sistema'
    for multa in multas:
        valor = multas[multa]
        if multa == placa:
            busca = f'A placa {placa} tem uma multa de R${valor:.2f}'
    return busca

def listaMulta(multas):
    for multa in multas:
        valor = multas[multa]
        print(f'{multa}: {valor:.2f}')

def placaMultaMaxMin(multas):
    max = 0
    min = 9999999
    multaMin = None
    multaMax = None

    for multa in multas:
        valor = multas[multa]
        
        if valor >= max:
            max = valor
            multaMax = multa

        if valor <= min:
            min = valor
            multaMin = multa
    return max, multaMax, min, multaMin
        

def calcMediaMultas(multas):
    cont = 0
    soma = 0
    for multa in multas:
        valor = multas[multa]
        cont += 1
        soma += valor
    media = soma / cont
    return media


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
    
    elif menu == 3:
        listaMulta(multas)
    elif menu == 4:
        max, multaMax, min, multaMin = placaMultaMaxMin(multas)
        print(f'Max - {multaMax}: {max}\nMin - {multaMin}: {min}')
    elif menu == 5:
        print(f'O valor médio das multas é: R${calcMediaMultas(multas):.2f}')
    elif menu == 6:
        break
    