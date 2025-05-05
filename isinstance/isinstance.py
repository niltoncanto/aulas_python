faltas = 10 #inteiro
preco = 10.0 #float
livro = ["senhor dos aneix","revolução dos bichos"] #lista
cadastro = {"nome":"joão","cpf":"095000000"} #dicionario

print(isinstance(faltas,int))
print(isinstance(preco,(int,float)))
print(isinstance(livro,list))
print(isinstance(cadastro,dict))

class Carro:
    def __init__(self,cor):
        self.cor = cor

carro = Carro("vermelha")
print(isinstance(carro,Carro))