
#manipulação de arquivos em python.

#abrir o arquivo para leitura ou escrita:
arquivo = open("arquivo.txt", "w") #w cria ou sobrescreve arquivo  'a' adiciona no arquivo  'r' somente leitura
arquivo.write("linha 1 #posiciona o ponteiro em um ponto do arquivo e inicia a leitura\n ")
arquivo.close()

arquivo = open("arquivo.txt","r") #abrindo somente para leitura
conteudo = arquivo.read()
print(conteudo)
print('\n')
#método moderno e correto de manipular arquivos em python:
with open("arquivo.txt", "a") as f:
    f.write("linha 2 #posiciona o ponteiro em um ponto do arquivo e inicia a leitura\n")
    f.write("linha 3 #posiciona o ponteiro em um ponto do arquivo e inicia a leitura\n")
    f.write("linha 4 #posiciona o ponteiro em um ponto do arquivo e inicia a leitura\n")
    f.write("linha 5 #posiciona o ponteiro em um ponto do arquivo e inicia a leitura\n")
    f.write("linha 6 #posiciona o ponteiro em um ponto do arquivo e inicia a leitura\n")
print('\n')
#lendo o conteúdo do arquivo
with open("arquivo.txt", "r") as f:
    conteudo = f.read()
    print(conteudo)
print('\n')
#lendo a primeira linha do arquivo
with open("arquivo.txt", "r") as f:
    linha = f.readline()
    print(linha)
print('\n')
#iterando sobre as linhas do arquivo
with open("arquivo.txt",'r') as f: 
    for linha in f.readlines():
        print(linha.rstrip())
print('\n')
#iterando diretamente sobre o objeto arquivo, o conteúdo do arquivo não é carregado totalmente na memória.
with open("arquivo.txt", "r") as f:
    for linha in f:
        print(linha.rstrip())
print('\n')
#le as primeira 3 linhas do arquivo
with open("arquivo.txt", "r") as f:
    linhas = f.readlines()[:3]  # Lê apenas as primeiras 5 linhas do arquivo
    for linha in linhas:
        print(linha.strip())  
print('\n')
#le a terceira e quarta linha do arquivo
with open("arquivo.txt", "r") as f:
    linhas = f.readlines()[2:4]  # Lê apenas as primeiras 5 linhas do arquivo
    for linha in linhas:
        print(linha.strip())   
print('\n')
#le os 15 primeiros caracteres do arquivo
with open("arquivo.txt", "r") as f:
    conteudo = f.read(5)  
    print(conteudo)
print('\n')
#posiciona o ponteiro em um ponto do arquivo e inicia a leitura
with open("arquivo.txt", "r") as f:
    f.seek(35)  # Move o cursor para o byte 15
    parte_do_arquivo = f.read(10)  # Lê 10 caracteres a partir do byte 50
    print(parte_do_arquivo)

dicionario = {"Nome":"José","idade":20}

import pickle
with open("arquivo.txt",'wb') as f: #abre para escrita binária
    pickle.dump(dicionario,f)
with open("arquivo.txt",'rb') as f:
    dicionario_lido = pickle.load(f)
    print(dicionario_lido)

import json
# Salvando um dicionário em formato JSON (legível)
with open('arquivo.json', 'w', encoding='utf-8') as f:
    json.dump(dicionario, f, indent=4)

# Lendo o dicionário de volta do arquivo JSON
with open('arquivo.json', 'r') as f:
    dicionario_lido = json.load(f)
    print(dicionario_lido)



