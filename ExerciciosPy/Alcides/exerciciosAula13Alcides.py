"""
1 - Faça um programa em Python que apresente o menu abaixo:
1 – Cadastrar multa (placa, valor)
2 – Buscar multa pela placa
3 – Listar todas as multas
4 – Exibir placa/multa referente ao valor mais alto e mais baixo
5 – Calcular o valor médio de todas as multas
6 – Sair
Utilize obrigatoriamente um dicionário para armazenar os dados e implemente uma função para cada item do menu.
O dicionário deve ser inicializado com os valores abaixo:
"""
"""

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

    """

"""
2 - Sistema de controle de estoque

"""
def cadastrarProd(produtos, nome, preco, qnt, cod):
    produtos[cod] = {
        "nome": nome,
        "preco": preco,
        "quantidade": qnt
    }
    return f'O produto {nome}, codigo {cod}, foi cadastrado '

def buscarProdCod(cod, produtos):
    if cod in produtos:
        nome = produtos[cod]["nome"]
        preco = produtos[cod]["preco"]
        qnt = produtos[cod]["quantidade"]
        resposta = f'nome: {nome}\npreco: R${preco:.2f}\nquantidade: {qnt}'
    else:
        resposta = f'Codigo informado não existe'
    return resposta

def venda(cod, qnt, produtos):
    if cod not in produtos:
        resposta = f'Codigo informado não existe'
    elif produtos[cod]["quantidade"] < qnt:
        resposta = f'O produto não tem a quantidade desejada em estoque para a venda\nQuantidade do produto {produtos[cod]["nome"]}: {produtos[cod]["quantidade"]}'
    else:
        produtos[cod]["quantidade"] = produtos[cod]["quantidade"] - qnt
        resposta = f'Venda do produto {produtos[cod]["nome"]} realizada!'

    return resposta
def reposicao(cod, qnt, produtos):
    if cod in produtos:
        produtos[cod]["quantidade"] += qnt
        resposta = f'Reposição registrada!\nNova quantidade do produto {produtos[cod]["nome"]}: {produtos[cod]["quantidade"]}'
    else:
        resposta = f'Codigo informado não existe'
    return resposta
def listarProd(produtos):
    for produto in produtos:
        nome = produtos[produto]["nome"]
        preco = produtos[produto]["preco"]
        qnt = produtos[produto]["quantidade"]
        print(f'{produto} - nome: {nome} - preco: R${preco:.2f} - quantidade {qnt}')
def prodSemEstq(produtos):
    pass
def prodMaiorVal(produtos):
    pass
def valorTotalEstq(produtos):
    pass



produtos = {
"P001": {"nome": "Teclado", "preco": 120.00, "quantidade": 8},
"P002": {"nome": "Mouse", "preco": 75.50, "quantidade": 15},
"P003": {"nome": "Monitor", "preco": 950.00, "quantidade": 4},
"P004": {"nome": "Webcam", "preco": 210.00, "quantidade": 0},
"P005": {"nome": "Headset", "preco": 180.00, "quantidade": 6}
}
while True:
    menu = int(input('1 - Cadastrar produto\n2 - Buscar produto pelo código\n3 - Registrar venda\n4 - Repor estoque\n5 - Listar produtos\n6 - Exibir produtos sem estoque\n7 - Exibir produto de maior valor em estoque\n8 - Exibir valor total do estoque\n9 – Sair\nQual opção você quer: '))

    if menu == 1:
        nome = str(input('Qual o nome do produto: '))
        preco = float(input('Qual o preço: '))
        qnt = int(input('Qual a quantidade disponivel: '))
        cod = str(input('Informe o codigo unico para cadastro do produto no formato PXXX (Ex. P001, P002, P010, P100, Etc): '))
        while cod in produtos:
            print(f'O codigo informado já esta sendo utilizado, por favor, tente outro\nCodigos ja sendo usados:')
            for codigo in produtos:
                print(f'{codigo}')
            cod = str(input('Informe o codigo unico para cadastro do produto no formato PXXX (Ex. P001, P002, P010, P100, Etc): '))
        print(cadastrarProd(produtos,nome,preco,qnt,cod))
            
    elif menu == 2:
        cod = str(input('Informe o codigo do produto para a busca no formato PXXX (Ex. P001, P002, P010, P100, Etc): '))
        print(buscarProdCod(cod, produtos))


    elif menu == 3:
        cod = str(input('Informe o codigo para a venda do produto no formato PXXX (Ex. P001, P002, P010, P100, Etc): '))
        qnt = int(input('Qual a quantidade do produto desejada para a venda: '))
        print(venda(cod, qnt, produtos))
    elif menu == 4:
         cod = str(input('Informe o codigo para a reposição do produto no formato PXXX (Ex. P001, P002, P010, P100, Etc): '))
         qnt = int(input('Qual a quantidade do produto foi recebida: '))
         print(reposicao(cod, qnt, produtos))
    elif menu == 5:
        listarProd(produtos)
    elif menu == 6:
        continue
    elif menu == 7:
        continue
    elif menu == 8:
        continue
    elif menu == 9:
        continue