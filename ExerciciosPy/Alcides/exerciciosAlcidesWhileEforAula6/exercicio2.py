"""
 Escreva um programa em Python que leia o gênero e a altura de N pessoas, calcule e mostre a altura média
das mulheres e dos homens separadamente. Utilize o comando de repetição que desejar


homens = int()
mulheres = int()
genero = int()
alturaH = float()
alturaM = float()
continuar = 's'


while continuar == 's':
    genero = int(input('Qual seu gênero? (masculino = 1, feminino = 2): '))
    if genero == 1:
        alturaH = alturaH + float(input('Qual sua altura?')) 
        homens += 1
    else:
        alturaM = alturaM + float(input('Qual sua altura?'))
        mulheres += 1
    continuar = str(input('Quer continuar? (s OU n): '))

mediaH = alturaH / homens
mediaM = alturaM / mulheres
print(f'Média da altura dos homens: {mediaH:.2f}Cm\nMédia da altura dos homens: {mediaH:.2f}Cm')

"""

mulher = int()
homem = int()
alturaH = int()
alturaM = int()
resp = 's'

while resp == 's':
    genero = str(input('genero: '))
    if genero == 'mulher':
        mulher += 1
        alturaM = int(input('altura: ')) + alturaM
    elif genero == 'homem':
        homem += 1
        alturaH = int(input('altura: ')) + alturaH
    resp = str(input('quer continuar? : '))

print('altura média')
print(f'homens: {alturaH/homem}cm')
print(f'mulheres: {alturaM / mulher}cm')
