def matricularAluno(turma ,ra, nome, nota1, nota2, faltas):
    for aluno in turma:
        if ra in aluno[0]:
            return f'RA ja existe no sistema!'
    turma.append([ra, nome, nota1, nota2, faltas])
    return f'O aluno {nome} foi cadastrado no sistema!'
def buscarAluno(turma, ra):
    for aluno in turma:
        if ra in aluno[0]:
              return aluno
    return f'Aluno não esta no sistema'
def lancarFalta(turma, ra, faltas):
    for aluno in turma:
        if ra in aluno[0]:
            aluno[4] += faltas
            return f'Faltas do aluno {aluno[1]} RA: {ra} foram atualizadas para {aluno[4]}'
    return f'Aluno não esta no sistema'
def atualizarNota(turma, aluno, nota):
       pass
def relatorioSitTurma(turma):
       pass
def alunoMaiorMed(turma):
       pass

turma = [
    ["RA01", "Ana Silva", 8.5, 9.0, 2],
    ["RA02", "Bruno Costa", 5.0, 6.0, 8],
    ["RA03", "Carla Dias", 9.5, 8.5, 0],
    ["RA04", "Daniel Souza", 4.0, 5.5, 16],
    ["RA05", "Elena Rocha", 7.0, 6.5, 4]
]

while True:
    menu = int(input('1-Matricular aluno\n2-Buscar aluno pelo RA\n3-Lançar faltas\n4-Atualizar nota\n5-Relatório de situação da turma\n6-Exibir aluno com a maior média\n7-Sair\nInforme a opção desejada: '))
    if menu > 7 or menu < 1:
        print('\nInforme uma opção valida!\n')
    elif menu == 1:
        ra = str(input('RA: '))
        nome = str(input('Nome: '))
        nota1 = float(input('Nota 1: '))
        nota2 = float(input('Nota 2: '))
        faltas = int(input('faltas: '))
        print(matricularAluno(turma ,ra, nome, nota1, nota2, faltas))
    elif menu == 2:
        ra = str(input('Qual o RA do aluno: '))
        print(buscarAluno(turma, ra))
    elif menu == 3:
         ra = str(input('Qual o RA do aluno: '))
         faltas = int(input('Numero de faltas a adicionar: '))
         print(lancarFalta(turma, ra, faltas))

    elif menu == 4:
            pass
    elif menu == 5:
            pass
    elif menu == 6:
            pass
    elif menu == 7:
            break