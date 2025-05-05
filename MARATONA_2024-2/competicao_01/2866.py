# Leitura do número de mensagens a serem codificadas
C = int(input())

# Leitura das mensagens codificadas
mensagens_codificadas = []
for _ in range(C):
    mensagem = input()
    mensagens_codificadas.append(mensagem)

def extrair_texto_oculto(mensagem):
    # Extrai caracteres em minúscula e os reverte
    caracteres_ocultos = []
    for char in reversed(mensagem):
        if char.islower():
            caracteres_ocultos.append(char)
    return ''.join(caracteres_ocultos)

# Processamento para extrair textos ocultos
textos_ocultos = []
for mensagem in mensagens_codificadas:
    texto_oculto = extrair_texto_oculto(mensagem)
    textos_ocultos.append(texto_oculto)

# Impressão dos textos ocultos
for texto in textos_ocultos:
    print(texto)
