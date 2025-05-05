import os
import stat
import pickle

class GerenciarArquivos:
    def __init__(self, nome_arquivo):
        self.nome_arquivo = nome_arquivo

    def escrever_arquivo(self, conteudo, modo='w'):
        """Escreve ou adiciona conteúdo a um arquivo"""
        try:
            with open(self.nome_arquivo, modo) as arquivo:
                arquivo.write(conteudo)
            print(f"Conteúdo escrito com sucesso no arquivo {self.nome_arquivo}.")
        except Exception as e:
            print(f"Erro ao escrever no arquivo {self.nome_arquivo}: {e}")

    def ler_arquivo(self):
        """Lê e retorna todo o conteúdo do arquivo"""
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                conteudo = arquivo.read()
            print(f"Conteúdo do arquivo {self.nome_arquivo}:")
            print(conteudo)
            return conteudo
        except Exception as e:
            print(f"Erro ao ler o arquivo {self.nome_arquivo}: {e}")
            return None

    def ler_primeira_linha(self):
        """Lê e imprime a primeira linha do arquivo"""
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                linha = arquivo.readline()
            print(f"Primeira linha do arquivo {self.nome_arquivo}: {linha}")
            return linha
        except Exception as e:
            print(f"Erro ao ler a primeira linha do arquivo {self.nome_arquivo}: {e}")
            return None

    def ler_linhas(self):
        """Lê o arquivo linha por linha e imprime cada uma"""
        try:
            with open(self.nome_arquivo, 'r') as arquivo:
                linhas = arquivo.readlines()
            print(f"Linhas do arquivo {self.nome_arquivo}:")
            for linha in linhas:
                print(linha)
            return linhas
        except Exception as e:
            print(f"Erro ao ler linhas do arquivo {self.nome_arquivo}: {e}")
            return None

    def informacoes_arquivo(self):
        """Imprime as informações do arquivo"""
        try:
            estatisticas = os.stat(self.nome_arquivo)
            informacoes = {
                'Tamanho': estatisticas[stat.ST_SIZE],
                'Última Modificação': estatisticas[stat.ST_MTIME],
                'Último Acesso': estatisticas[stat.ST_ATIME],
                'Data de Criação': estatisticas[stat.ST_CTIME],
                'Modo': estatisticas[stat.ST_MODE]
            }
            print(f"Informações do arquivo {self.nome_arquivo}:")
            for chave, valor in informacoes.items():
                print(f"{chave}: {valor}")
            return informacoes
        except Exception as e:
            print(f"Erro ao obter informações do arquivo {self.nome_arquivo}: {e}")
            return None

    def listar_diretorio(self):
        """Lista os arquivos e pastas no diretório atual"""
        try:
            diretorio_atual = os.path.dirname(os.path.abspath(__file__))
            arquivos = os.listdir(diretorio_atual)
            print(f"Arquivos no diretório {diretorio_atual}:")
            for arquivo in arquivos:
                print(arquivo)
            return arquivos
        except Exception as e:
            print(f"Erro ao listar o diretório: {e}")
            return None

    def gravar_com_pickle(self, dados):
        """Grava dados em um arquivo usando pickle (serialização)"""
        try:
            with open(self.nome_arquivo, 'wb') as arquivo:
                pickle.dump(dados, arquivo)
            print(f"Dados gravados com sucesso no arquivo {self.nome_arquivo} usando pickle.")
        except Exception as e:
            print(f"Erro ao gravar dados com pickle no arquivo {self.nome_arquivo}: {e}")

    def ler_com_pickle(self):
        """Lê dados de um arquivo usando pickle (desserialização)"""
        try:
            with open(self.nome_arquivo, 'rb') as arquivo:
                dados = pickle.load(arquivo)
            print(f"Dados lidos com sucesso do arquivo {self.nome_arquivo} usando pickle.")
            print(dados)
            return dados
        except Exception as e:
            print(f"Erro ao ler dados com pickle no arquivo {self.nome_arquivo}: {e}")
            return None

# Exemplo de uso da classe GerenciarArquivos
gerenciador = GerenciarArquivos('teste.txt')

# Escrever conteúdo no arquivo
gerenciador.escrever_arquivo("escrevendo mais uma linha 1\n", modo='w')
gerenciador.escrever_arquivo("escrevendo mais uma linha 2\n", modo='a')
gerenciador.escrever_arquivo("escrevendo mais uma linha 3\n", modo='a')

# Ler conteúdo do arquivo
gerenciador.ler_arquivo()

# Ler a primeira linha
gerenciador.ler_primeira_linha()

# Ler todas as linhas do arquivo
gerenciador.ler_linhas()

# Obter informações sobre o arquivo
gerenciador.informacoes_arquivo()

# Listar arquivos no diretório
gerenciador.listar_diretorio()

# Gravar e ler dados com pickle
gerenciador_pickle = GerenciarArquivos('arquivo_pickle.txt')
gerenciador_pickle.gravar_com_pickle([1, 2, 3, 4, 5])
gerenciador_pickle.ler_com_pickle()
