"""
a) Você recebeu uma lista com as temperaturas registradas durante uma semana, onde cada elemento representa a
temperatura média de um dia.
temperaturas = [22, 24, 21, 20, 19, 23, 25]
Tarefas:
- Exiba as temperaturas dos três primeiros dias da semana.
- Exiba as temperaturas dos dois últimos dias.
- Exiba as temperaturas dos dias ímpares da semana (considerando o índice, ou seja, posição 1, 3, 5).
- Inverta a ordem da lista utilizando fatiamento.


temperaturas = [22, 24, 21, 20, 19, 23, 25]
print(temperaturas[0:3])
print(temperaturas[len(temperaturas)-2:len(temperaturas)])
print(temperaturas[1:len(temperaturas):2])
print(temperaturas[len(temperaturas)::-1])
"""



"""
b) Dada a string abaixo:
frase = "Programação em Python é divertida!“
Tarefas:
- Exiba os primeiros 12 caracteres da frase.
- Exiba os últimos 9 caracteres da frase.
- Exiba a frase pulando uma letra (um caractere sim, outro não).
- Inverta toda a string usando fatiamento.

frase = 'Programação em Python é divertida!'

print(frase[0:12])
print(frase[len(frase)-9:len(frase)])
print(frase[0:len(frase):2])
print(frase[len(frase)::-1])
"""




"""
Uma empresa de tecnologia deseja analisar mensagens de log geradas por seu sistema de
atendimento automático. Cada mensagem contém informações textuais que devem ser processadas
utilizando operações com strings e listas, sem uso de estruturas avançadas como dicionários ou
bibliotecas externas. Você receberá uma lista de mensagens no seguinte formato:
mensagens = [
 "ERRO: Falha ao conectar no servidor",
 "OK: Operação realizada com sucesso",
 "ALERTA: Uso de memória alto",
 "ERRO: Timeout na requisição",
 "OK: Dados processados",
 "ALERTA: CPU em nível crítico"
]
EXERCÍCIO 2 23
Objetivo
Desenvolver um programa que analise essas mensagens e gere informações estratégicas para o sistema.
Requisitos
• Separação das categorias
• Crie uma função: def classificar_mensagens(lista):
• Ela deve:
• Criar três listas:
• erros
• alertas
• sucessos
• Utilizar:
• fatiamento ou métodos de string (find, in, etc.)
• Retornar as três listas
EXERCÍCIO 2 24
Normalização das mensagens • Crie uma função: def normalizar_mensagem(msg): • Ela deve: • Remover espaços extras (strip) • Converter tudo para minúsculo (lower) • Retornar a mensagem tratada
Extração do conteúdo (uso de fatiamento) • Crie uma função: def extrair_conteudo(msg): • Ela deve: • Retirar o prefixo ("ERRO:", "OK:", "ALERTA:") • Retornar apenas o conteúdo da mensagem • Obrigatório usar fatiamento (slice)
EXERCÍCIO 2 25
Estatísticas do sistema
• Crie uma função: def gerar_estatisticas(erros, alertas, sucessos):
• Ela deve:
• Calcular:
• total de mensagens
• quantidade de erros
• quantidade de alertas
• quantidade de sucessos
• Retornar uma string formatada com os resultados
Busca inteligente
• Crie uma função: def buscar_palavra(lista, palavra):
• Ela deve:
• Verificar em quantas mensagens a palavra aparece
• Usar operador in
• Retornar a quantidade encontrada
EXERCÍCIO 2 26
Programa principal (main
)
• O programa deve: • Classificar as mensagens • Normalizar todas • Extrair apenas o conteúdo • Exibir: • listas separadas • estatísticas • resultado da busca pela palavra "erro"
"""
def classificar_mensagens(lista):
    erros = []
    alertas = []
    sucessos = []
    for mensagem in lista:
        if 'ERRO' in mensagem:
            erros.append(mensagem)
        elif 'ALERTA' in mensagem:
            alertas.append(mensagem)
        else:
            sucessos.append(mensagem)
    return erros,alertas,sucessos

def normalizar_mensagem(msg):
    return msg.strip().lower()

def extrair_conteudo(msg):
    indice = msg.find(':')
    conteudo = msg[indice+1:]
    return conteudo


def gerar_estatisticas(erros, alertas, sucessos):
    totalErros = len(erros)
    totalAlertas = len(alertas)
    totalSucessos = len(sucessos)
    totalMsg = totalErros + totalAlertas + totalSucessos

    return f'Total: {totalMsg}\nErros: {totalErros}\nAlertas: {totalAlertas}\nSucessos: {totalSucessos}'

def buscar_palavra(lista, palavra):
    cont = 0
    for msg in lista:
        if palavra in msg.lower():
            cont += 1
    return cont

mensagens = [
 "ERRO: Falha ao conectar no servidor",
 "OK: Operação realizada com sucesso",
 "ALERTA: Uso de memória alto",
 "ERRO: Timeout na requisição",
 "OK: Dados processados",
 "ALERTA: CPU em nível crítico"
]

erros, alertas, sucessos = classificar_mensagens(mensagens)
msgs_normalizadas = []
conteudos = []
for msg in mensagens:
    msg_normalizada = normalizar_mensagem(msg)
    msgs_normalizadas.append(msg_normalizada)
    conteudo = extrair_conteudo(msg)
    conteudos.append(conteudo)

print(f'=== LISTAS ===')
print(f'Erros: {erros}\nAlertas: {alertas}\nSucessos: {sucessos}')
print(f'=== MENSAGENS NORMALIZADAS ===')
print(msgs_normalizadas)
print(f'=== CONTEÚDO ===')
print(conteudos)
print(f'=== RELATÓRIO ===')
print(f'{gerar_estatisticas(erros, alertas, sucessos)}')
print("Ocorrências da palavra"+" '"+"erro"+"'"+":", buscar_palavra(mensagens,'erro'))
