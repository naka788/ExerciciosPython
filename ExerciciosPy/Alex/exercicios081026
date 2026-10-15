def reajuste(salario):
    if salario >= 3000.0:
        reajuste = salario + (salario * 0.45)
    elif salario < 3000.0 and salario >= 2000.0:
        reajuste = salario + (salario * 0.65)
    else:
        reajuste = salario + (salario * 0.85)
    return reajuste

def reajusteMedioMasc(salario):
    
empregados65 = 0
while True:
    nome = str(input('nome: '))
    sexo = str(input('sexo: '))
    while sexo != 'F' and sexo != 'M':
        print('Sexo inválido! M ou F')
        sexo = str(input('sexo: '))
    salario = float(input('salario: '))
    while salario < float(850.0):
        print('Salário muito pequeno aceitar apenas acima de R$850,00')
        salario = float(input('salario: '))
    if salario < 3000.0 and salario >= 2000.0:
        empregados65 += 1
    """
    if sexo == 'M':
    """
        
    print(f'salario reajustado: R${reajuste(salario):.2f}')
    print(f'empregados com reajuste de 6,5%: {empregados65}')
    
    

    
