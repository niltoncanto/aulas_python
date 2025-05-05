# Classe GerenciarArquivo
import os

class GerenciarArquivo:

    @staticmethod
    def gravar(dados, filename="formas.txt"):
        with open(filename, 'a') as file:
            file.write(dados + '\n')

    @staticmethod
    def ler(filename="formas.txt"):
        if os.path.exists(filename):
            with open(filename, 'r') as file:
                return file.read()
        else:
            return "Arquivo não encontrado."