import statistics
from datetime import datetime, timedelta

def classificacao (peso, altura):
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

    novoImc = peso / (altura**2) - ((peso / (altura**2)) * 0.05)
    novaPressaoSisto = pressaoSisto - (pressaoSisto * 0.05)
    if nivelAtv >= 9:
        novoNivelAtv = 10
        
    else:
        novoNivelAtv = nivelAtv + 2

    novoConsumoAlcoSemana = consumoAlcoSemana - (consumoAlcoSemana * 0.2)
    riscoRecalM = (novoImc * 0.3) + (novaPressaoSisto / 120 * 0.3) + ((10 - novoNivelAtv) * 0.2) + (novoConsumoAlcoSemana / 10 * 0.2)
    return riscoRecalM

def piora (peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana):
    novoImc = peso / (altura**2) + ((peso / (altura**2)) * 0.05)
    novaPressaoSisto = pressaoSisto + (pressaoSisto * 0.05)
    if nivelAtv <= 0:
        novoNivelAtv = nivelAtv
    else:
        novoNivelAtv = nivelAtv - 2

    novoConsumoAlcoSemana = consumoAlcoSemana + (consumoAlcoSemana * 0.2)
    riscoRecalP = (novoImc * 0.3) + (novaPressaoSisto / 120 * 0.3) + ((10 - novoNivelAtv) * 0.2) + (novoConsumoAlcoSemana / 10 * 0.2)
    return riscoRecalP

def classFinal(media):
    if media < 5:
        classF = 'Baixo risco'
    elif media >= 5 and media <= 8:
        classF = 'Médio risco'
    else:
        classF = 'Alto risco'

    return classF

def avalObj(objSaude, media, risco):
    if objSaude == 1:
        if media < 5:
            return 'Sim'
        else:
            return 'Não'
        
    elif objSaude == 2:
        if media <= 8:
            return 'Sim'
        else:
            return 'Não'
        
    elif media <= risco:
        return 'Sim'
    else:
        return 'Não'

def dataAval():
    hoje = datetime.now()
    diasReaval = timedelta(days=90)
    dataReaval = hoje + diasReaval
    reaval = dataReaval.strftime("%d/%m/%y")
    return reaval


nome = str(input('nome paciente: '))
idade = int(input('idade: '))
peso = float(input('peso (kg): '))
altura = float(input('altura (m): '))
pressaoSisto = float(input('Pressão sistólica (mmHg): '))
pressaoDiast = float(input('Pressão diastólica (mmHg): '))
nivelAtv = int(input('Nível de atividade física (0 a 10): '))
consumoAlcoSemana = int(input('Consumo de álcool semanal (unidades): '))
objSaude = int(input('Objetivo de saúde desejado (1- Reduzir para baixo risco |2- Reduzir para médio risco |3- Manter estado atual):'))

risco = ((peso / (altura**2)) * 0.3) + (pressaoSisto / 120 * 0.3) + ((10 - nivelAtv) * 0.2) + (consumoAlcoSemana / 10 * 0.2)
riscoRecalM = melhoria(peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana)
riscoRecalP = piora(peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana)
todosRiscos = [risco, riscoRecalM, riscoRecalP]
media = statistics.mean(todosRiscos)
mediana = statistics.median(todosRiscos)
desvio = statistics.stdev(todosRiscos)
dataHoje = datetime.now()
print(f'Paciente: {nome}')
print(f'Data: {dataHoje.strftime("%d/%m/%y")}')
print(f'Reavaliação: {dataAval()}')
print('')
print(f'IMC: {(peso / (altura**2)):.2f} - {classificacao(peso, altura)}')
print(f'Pressão: {pressaoSisto}/{pressaoDiast} - {pressao(pressaoSisto, pressaoDiast)}')
print('')
print(f'Risco Atual: {risco:.2f}')
print(f'Melhoria: {melhoria(peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana):.2f}')
print(f'Estavél: {risco:.2f}')
print(f'Piora: {piora(peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana):.2f}')
print('')
print(f'Média: {media:.2f}')
print(f'Mediana: {mediana:.2f}')
print(f'Desvio: {desvio:.2f}')
print('')
print(f'Classificação: {classFinal(media)}')
print(f'Objetivo atingido: {avalObj(objSaude, media, risco)}')
print('')
print(f'Melhor cenário: {melhoria(peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana):.2f}')
print(f'Pior cenário: {piora(peso, altura, pressaoSisto, nivelAtv, consumoAlcoSemana):.2f}')

