'''
valor = int(input('insira valor: '))

soma = 1
for i in range(2, valor+1):
    soma += 1/i
    print(f'1/{i}={soma}')

print('final: ', soma)
'''

'''
def fatorial(numero):
    fatorial = 1
    for num in range(1, numero+1):
        fatorial = fatorial * num
    return fatorial

numero = int(input('numero para fazer fatorial: '))
print(f'{fatorial(numero)}')
'''

'''
contador = 20
soma = 0
for numero in range(20,400+1):
    if (numero % 2) == 0:
        contador += 1
        soma = soma + numero
    else:
        contador +=1
print(contador)
print(soma)
'''

pessoasMaior50 = 0 
pessoasEntre10e20 = 0
soma10e20 = 0
pessoasMenor40 = 0
for i in range(0,5+1):
    idade = int(input('idade: '))
    if idade >= 10 and idade <= 20:
        pessoasEntre10e20 += 1
        altura = int(input('altura (cm): '))
        soma10e20 += altura
        peso = float(input('peso em kg: '))
        if peso < 40:
            pessoasMenor40 += 1
    elif idade > 50:
        pessoasMaior50 += 1
    
    altura = int(input('altura (cm): '))
    peso = float(input('peso em kg: '))
    if peso < 40:
        pessoasMenor40 += 1

mediaAltura = soma10e20 / pessoasEntre10e20
percPessoasMenor40 = (pessoasMenor40 / 30) * 100
print(f'a) {pessoasMaior50}')
print(f'b) {mediaAltura}')
print(f'c) {percPessoasMenor40}%')
"""
esta errado, arrumar
"""