def imc (peso, altura):
    imc = peso / (altura**2)
    if imc >= 30:
        classificacao = 'Obesidade'
    elif imc >= 25 and imc <= 29.9:
        classificacao = 'Sobrepreso'
    elif imc >= 18.5 and imc <= 24.9:
        classificacao = 'Normal'
    else:
        classificacao = 'Abaixo do peso'

    return classificacao

def pressao (pressaoSisto, pressaoDiast):
    if pressaoSisto < 120 and pressaoDiast < 80:
        pressao = 'Normal'
    elif pressaoSisto >= 120 and pressaoSisto < 130 and pressaoDiast < 80:
        pressao = 'Elevada'
    elif pressaoSisto >= 130 or pressaoDiast > 80:
        pressao = 'Hipertensão'

    return pressao

def melhoria (peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana):

    novoImc = imc(peso, altura) - (imc(peso,altura) * 0.05)
    novaPressaoSisto = pressaoSisto - (pressaoSisto * 0.05)
    if nivelAtv >= 9:
        novoNivelAtv = 10
        
    else:
        novoNivelAtv = nivelAtv + 2
    novoConsumoAlcoSemana = consumoAlcoSemana - (consumoAlcoSemana * 0.2)
    riscoRecal = (novoImc * 0.3) + (novaPressaoSisto / 120 * 0.3) + ((10 - novoNivelAtv) * 0.2) + (novoConsumoAlcoSemana / 10 * 0.2)
    return riscoRecal
"""
def estabilidade
"""
nome = str(input('nome paciente: '))
idade = int(input('idade: '))
peso = float(input('peso (kg): '))
altura = float(input('altura (m): '))
pressaoSisto = float(input('Pressão sistólica (mmHg): '))
pressaoDiast = float(input('Pressão diastólica (mmHg): '))
nivelAtv = int(input('Nível de atividade física (0 a 10): '))
consumoAlcoSemana = int(input('Consumo de álcool semanal (unidades): '))
objSaude = int(input('Objetivo de saúde desejado (1- Reduzir para baixo risco |2- Reduzir para médio risco |3- Manter estado atual):'))

risco = (imc(peso, altura) * 0.3) + (pressaoSisto / 120 * 0.3) + ((10 - nivelAtv) * 0.2) + (consumoAlcoSemana / 10 * 0.2)

