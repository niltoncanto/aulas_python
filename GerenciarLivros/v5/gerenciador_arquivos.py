import os
import shutil

class Gerenciador:
    def gravar(self,nome_arquivo,conteudo):
        try:
            with open(nome_arquivo,'a') as f:
                f.write(conteudo)
                return "Conteúdo gravado com sucesso!"
        except FileNotFoundError:
            return "Arquivo não encontrado!"
        except PermissionError:
            return "vc não tem permissão para gravar neste arquivo."
        except Exception:
            return "erro ao gravar no arquivo."
    def ler(self,arquivo):
        try:
            with open(nome_arquivo, 'r') as f:
                conteudo = f.read()
                return conteudo
        except FileNotFoundError:
            return "Arquivo não encontrado!"
        except PermissionError:
            return "vc não tem permissão de leitura."
        except Exception:
            return "erro ao gravar no arquivo."
    def renomear(self,nome_arquivo,novo_nome_arquivo):
        try:
            os.rename(nome_arquivo,novo_nome_arquivo)
            return "arquivo renomeado com sucesso!"
        except FileNotFoundError:
            return "Arquivo não encontrado!"
        except PermissionError:
            return "acesso negado."
        except Exception:
            return "erro ao renomear no arquivo."
    def deletar(self,nome_arquivo):
        try:
            os.remove(nome_arquivo, 'r')
        except FileNotFoundError:
            return "Arquivo não encontrado!"
        except PermissionError:
            return "vc não tem permissão para apagar arquivo."
        except Exception:
            return "erro."
        
    def lerLinhas(self,arquivo):
        try:
            with open(nome_arquivo, 'r') as f:
                linhas = f.readlines()
                for linha in linhas:
                    print(linha)
                return None
        except FileNotFoundError:
            return "Arquivo não encontrado!"
        except PermissionError:
            return "vc não tem permissão de leitura."
        except Exception:
            return "erro ao gravar no arquivo."