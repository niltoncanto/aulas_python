import os
import sys
import stat
import time
import pickle

# abrindo e escrevendo em arquivos
fileHandle = open('teste.txt','w')
fileHandle.write("escrevendo mais uma linha 1")
fileHandle.close()
fileHandle = open('teste.txt','a')
fileHandle.write("\nescrevendo mais uma linha 2")
fileHandle.write("\nescrevendo mais uma linha 3")
fileHandle.close()
print("\n")

# lendo arquivos
fileHandle = open('teste.txt','r')
print(fileHandle.read())
fileHandle.close()
print("\n")

# imprimindo a primeira linha
fileHandle = open('teste.txt','r')
linha=fileHandle.readline()
print(linha)
fileHandle.close()
print("\n")

# lendo arquivos linha a linha
fileHandle = open('teste.txt','r')
fileList = fileHandle.readlines()
for line in fileList:
    print(line)
fileHandle.close()
print("\n")

# observe que a primeira linha não é impressa
fileHandle = open('teste.txt','r')
garbage = fileHandle.readline()
linha=fileHandle.readline()
print(linha)
fileHandle.close()
print("\n")

# para imprimir a primeira linha novamente, é necessário voltar ao início do arquivo
fileHandle = open('teste.txt','r')
garbage = fileHandle.readline()
fileHandle.seek(0)
linha=fileHandle.readline()
print(linha)
fileHandle.close()

# imprimindo informações sobre o arquivo
fileStatsObj = os.stat ( 'teste.txt' )
print(fileStatsObj) # informações sobre o arquivo

fileInfo = {'Size': fileStatsObj [ stat.ST_SIZE ], 'LastModified': fileStatsObj [ stat.ST_MTIME ], 
            'LastAccessed': fileStatsObj [ stat.ST_ATIME ], 
            'CreationTime': fileStatsObj [ stat.ST_CTIME ], 
            'Mode': fileStatsObj [ stat.ST_MODE ]}
for k,v in fileInfo.items(): 
    print (k, ' = ', v)

if (stat.S_ISDIR(fileStatsObj [ stat.ST_MODE ])):
    print('é um diretório')
else:
    print('não é um diretório')

diretorio_atual = os.path.dirname(os.path.abspath(__file__))
for file in os.listdir(diretorio_atual):
    print(file)
print("\n")

# gravando informações em arquivo com o módulo pickle
fileHandle = open("pickleFile.txt", 'wb')
teste = [1,2,3,4,5]
pickle.dump(teste, fileHandle)
fileHandle.close()
print("\n")

#lendo informações de arquivo com o módulo pickle
fileHandle = open("pickleFile.txt", 'rb')
dados_lidos = pickle.load(fileHandle)
print(dados_lidos)  # Saída: [1, 2, 3, 4, 5]



