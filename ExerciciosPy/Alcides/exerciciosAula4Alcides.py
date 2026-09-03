'''
1- Escreva um código que solicite um número ao usuário. Caso seja digitado um valor entre 0 e 9,
mostre: “valor correto”, caso contrário mostre: “valor incorreto”

num = float(input('digite numero >> '))

if (num >= 0) and (num <= 9):
    print('valor correto')

else:
    print('valor incorreto')
'''

'''
2- Crie um código que solicite ao usuário o seu turno de trabalho e a quantidade de horas
trabalhadas, calcule e mostre o valor do salário. Considere os valores de horas a seguir, de acordo
com o turno de trabalho. Caso o turno seja igual a ‘N’ (utilize um caractere para representar) o valor
da hora trabalhada é R$ 45,00, caso contrário é R$ 37,50




h1 = int(input('que horas começa seu trabalho? >> '))
h2 = int(input('que horas acaba seu trabalho? >> '))
horasTrabalhadas = int(input('quantas horas voce trabalhou? >> '))
turnoTrab = h2 - h1
N = float(6)
salario = float(0)

if horasTrabalhadas <= turnoTrab:
    if(turnoTrab == N):
        salario = float(45.00)
        print(f'o seu salario é igual a {(salario) * horasTrabalhadas}')

    else:
        salario = float(37.50)
        print(f'o seu salario é igual a {((salario) * horasTrabalhadas):.2f}')
else:
    print('erro: voce trabalhou mais horas do que seu turno permite')

'''

