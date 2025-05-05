import os
import shutil

class GerenciadorDeArquivos:
    def __init__(self):
        pass
    def gravar_em_arquivo(self, nome_arquivo, conteudo):
        try:
            with open(nome_arquivo, 'w') as f:
                f.write(conteudo)
            print(f"Conteúdo gravado com sucesso em {nome_arquivo}!")
        except Exception as e:
            print(f"Erro ao gravar no arquivo: {e}")

    def ler_arquivo(self, nome_arquivo):
        try:
            with open(nome_arquivo, 'r') as f:
                conteudo = f.read()
            print(f"Conteúdo de {nome_arquivo}:\n{conteudo}")
        except FileNotFoundError:
            print(f"Arquivo {nome_arquivo} não encontrado.")
        except Exception as e:
            print(f"Erro ao ler o arquivo: {e}")

    def criar_diretorio(self, nome_diretorio):
        try:
            os.mkdir(nome_diretorio)
            print(f"Diretório {nome_diretorio} criado com sucesso!")
        except FileExistsError:
            print(f"Diretório {nome_diretorio} já existe.")
        except Exception as e:
            print(f"Erro ao criar o diretório: {e}")

    def listar_diretorio(self, nome_diretorio):
        try:
            with os.scandir(nome_diretorio) as entries:
                for entry in entries:
                    print(entry.name)
        except FileNotFoundError:
            print(f"Diretório {nome_diretorio} não encontrado.")
        except Exception as e:
            print(f"Erro ao listar o diretório: {e}")

    def apagar_diretorio(self, nome_diretorio):
        try:
            shutil.rmtree(nome_diretorio)
            print(f"Diretório {nome_diretorio} apagado com sucesso!")
        except FileNotFoundError:
            print(f"Diretório {nome_diretorio} não encontrado.")
        except Exception as e:
            print(f"Erro ao apagar o diretório: {e}")

    def renomear(self, nome_antigo, nome_novo):
        try:
            os.rename(nome_antigo, nome_novo)
            print(f"{nome_antigo} renomeado para {nome_novo} com sucesso!")
        except FileNotFoundError:
            print(f"{nome_antigo} não encontrado.")
        except Exception as e:
            print(f"Erro ao renomear: {e}")

    def palindromo(self,word):
        print(word , word[::-1])
        return word == word[::-1]
    
    def palindromo(self,word):
        print(word , reversed)
        return word == word[::-1]
    
if __name__ == "__main__":
    gerenciador = GerenciadorDeArquivos()
    gerenciador.criar_diretorio("meu_diretorio")
    gerenciador.gravar_em_arquivo("meu_diretorio/meu_arquivo.txt", "Olá, mundo!")
    gerenciador.listar_diretorio("meu_diretorio")
    gerenciador.ler_arquivo("meu_arquivo.txt")
    gerenciador.renomear("meu_diretorio/meu_arquivo.txt", "meu_diretorio/meu_novo_arquivo.txt")
    #gerenciador.apagar_diretorio("meu_diretorio")
    print(gerenciador.palindromo('ama'))
