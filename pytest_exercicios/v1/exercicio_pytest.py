# ExercicioPyTest.py
import os

class ExercicioPyTest:
    def soma(self, a, b):
        return a + b

    def concatena_strings(self, str1, str2):
        return str1 + str2

    def gravar_em_arquivo(self, texto, filename):
        with open(filename, 'w') as f:
            f.write(texto)
        return True

    def ler_de_arquivo(self, filename):
        if os.path.exists(filename):
            with open(filename, 'r') as f:
                return f.read()
        else:
            return "Arquivo não encontrado"

    def inverter_string(self, texto):
        return texto[::-1]

    def contar_vogais(self, texto):
        return sum(1 for char in texto if char.lower() in 'aeiou')

    def fatorial(self, n):
        if n == 0:
            return 1
        else:
            return n * self.fatorial(n-1)

    def eh_par(self, n):
        return n % 2 == 0

    def listar_arquivos(self, diretorio):
        return os.listdir(diretorio)

    def calcular_media(self, lista_numeros):
        return sum(lista_numeros) / len(lista_numeros)
