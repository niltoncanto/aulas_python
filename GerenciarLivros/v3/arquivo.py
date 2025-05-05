class Arquivo:
    def __init__(self,arquivo):
        self.arquivo = arquivo

    def gravar(self,dados):
        with open(self.arquivo, 'a') as file:
            file.write(dados + '\n')


    def ler(self):
        texto = ''
        with open(self.arquivo, 'r') as file:
            for linha in file:
                texto += linha
                #titulo,autor,isbn,status,x = linha.strip().split(', ')
        return texto #titulo,autor,isbn,status

    def lerLinha(self):
        arq = open(self.arquivo,'r')
        linha = arq.readline()
        arq.close()
        return linha

    def lerLinhas(self):
        arq = open(self.arquivo, 'r')
        linhas = arq.readlines()
        arq.close()
        return linhas
    
    def lerTudo(self):
        arq = open(self.arquivo, 'r')
        texto = arq.read()
        arq.close()
        return texto
    def lerWhile(self):
        linhas = []
        arq = open(self.arquivo, 'r')
        linha = arq.readline()
        while linha:
            linhas.append(linha)
        
        arq.close()
        return linhas