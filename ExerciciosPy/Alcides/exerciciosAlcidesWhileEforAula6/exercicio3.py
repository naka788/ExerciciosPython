maior = int()
menor = int()
num = int()
while num >= 0:
    num = int(input('numero: '))
    if num > maior:
        maior = num
    elif num < menor:
        menor = num
print(f'maior: {maior} | menor: {menor}')