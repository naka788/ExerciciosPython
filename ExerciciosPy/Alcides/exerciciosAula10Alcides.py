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

for i in range(0,30+1):
    idade = int(input('idade: '))
    if idade >= 10 and idade <= 20:
        altura = int(input('altura (cm): '))
        pessoasEntre10e20 += 1
        peso = float(input('peso em kg: '))
    elif idade > 50:
        pessoasMaior50 += 1
    
    altura = int(input('altura (cm): '))
    peso = float(input('peso em kg: '))
