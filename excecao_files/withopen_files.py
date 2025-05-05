import os
import stat
import pickle

# Abrindo e escrevendo em arquivos usando 'with'
with open('teste.txt', 'w') as manipulador_arquivo:  # Abre o arquivo "teste.txt" em modo de escrita
    manipulador_arquivo.write("escrevendo mais uma linha 1")  # Escreve uma linha no arquivo

with open('teste.txt', 'a') as manipulador_arquivo:  # Abre o arquivo "teste.txt" em modo de adição (append)
    manipulador_arquivo.write("\nescrevendo mais uma linha 2")  # Adiciona mais uma linha ao arquivo
    manipulador_arquivo.write("\nescrevendo mais uma linha 3")  # Adiciona outra linha ao arquivo
print("\n")

# Lendo arquivos usando 'with'
with open('teste.txt', 'r') as manipulador_arquivo:  # Abre o arquivo "teste.txt" em modo de leitura
    print(manipulador_arquivo.read())  # Lê e imprime todo o conteúdo do arquivo
print("\n")

# Imprimindo a primeira linha usando 'with'
with open('teste.txt', 'r') as manipulador_arquivo:  # Abre o arquivo "teste.txt" para leitura
    linha = manipulador_arquivo.readline()  # Lê a primeira linha do arquivo
    print(linha)  # Imprime a primeira linha
print("\n")

# Lendo arquivos linha por linha usando 'with'
with open('teste.txt', 'r') as manipulador_arquivo:  # Abre o arquivo "teste.txt" para leitura
    lista_linhas = manipulador_arquivo.readlines()  # Lê todas as linhas do arquivo e as armazena em uma lista
    for linha in lista_linhas:  # Itera sobre a lista de linhas
        print(linha)  # Imprime cada linha
print("\n")

# Observe que a primeira linha não é impressa (pois já foi lida no código anterior)
with open('teste.txt', 'r') as manipulador_arquivo:  # Abre o arquivo para leitura
    lixo = manipulador_arquivo.readline()  # Lê e descarta a primeira linha
    linha = manipulador_arquivo.readline()  # Lê a segunda linha
    print(linha)  # Imprime a segunda linha
print("\n")

# Para imprimir a primeira linha novamente, é necessário "voltar" ao início do arquivo
with open('teste.txt', 'r') as manipulador_arquivo:  # Abre o arquivo para leitura
    lixo = manipulador_arquivo.readline()  # Lê a primeira linha
    manipulador_arquivo.seek(0)  # Volta o cursor de leitura para o início do arquivo
    linha = manipulador_arquivo.readline()  # Lê a primeira linha novamente
    print(linha)  # Imprime a primeira linha

# Imprimindo informações sobre o arquivo
estatisticas_arquivo = os.stat('teste.txt')  # Obtém as estatísticas do arquivo (tamanho, datas, etc.)
print(estatisticas_arquivo)  # Imprime todas as informações coletadas sobre o arquivo

informacoes_arquivo = {  # Dicionário para organizar algumas informações importantes do arquivo
    'Tamanho': estatisticas_arquivo[stat.ST_SIZE],  # Tamanho do arquivo
    'Última Modificação': estatisticas_arquivo[stat.ST_MTIME],  # Data da última modificação
    'Último Acesso': estatisticas_arquivo[stat.ST_ATIME],  # Data do último acesso
    'Data de Criação': estatisticas_arquivo[stat.ST_CTIME],  # Data de criação
    'Modo': estatisticas_arquivo[stat.ST_MODE]  # Permissões e modo do arquivo
}
for chave, valor in informacoes_arquivo.items():  # Itera sobre as informações para imprimir
    print(chave, ' = ', valor)  # Imprime a chave e o valor correspondentes

# Verifica se o caminho é um diretório
if stat.S_ISDIR(estatisticas_arquivo[stat.ST_MODE]):
    print('é um diretório')  # Imprime se for um diretório
else:
    print('não é um diretório')  # Imprime se não for um diretório

# Listando arquivos no diretório atual
diretorio_atual = os.path.dirname(os.path.abspath(__file__))  # Obtém o diretório atual
for arquivo in os.listdir(diretorio_atual):  # Itera sobre os arquivos e pastas no diretório
    print(arquivo)  # Imprime o nome de cada arquivo ou pasta
print("\n")

# Gravando informações em arquivo com o módulo pickle usando 'with'
with open("arquivo_pickle.txt", 'wb') as manipulador_arquivo:  # Abre o arquivo em modo binário para escrita
    lista_teste = [1, 2, 3, 4, 5]  # Uma lista simples de números
    pickle.dump(lista_teste, manipulador_arquivo)  # Usa pickle para serializar a lista e gravá-la no arquivo
print("\n")

# Lendo informações de arquivo com o módulo pickle usando 'with'
with open("arquivo_pickle.txt", 'rb') as manipulador_arquivo:  # Abre o arquivo em modo binário para leitura
    dados_lidos = pickle.load(manipulador_arquivo)  # Carrega os dados de volta (deserializa)
    print(dados_lidos)  # Imprime a lista lida do arquivo (saída: [1, 2, 3, 4, 5])
