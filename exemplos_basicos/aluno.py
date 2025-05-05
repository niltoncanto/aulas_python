'''
Enunciado:  Você foi contratado para criar um sistema que gerencie os alunos de uma escola. 
O sistema deve ser capaz de adicionar alunos, limitando a quantidade com base na capacidade fornecida, 
e mostrar todos os alunos cadastrados. Implemente o sistema usando duas classes: Aluno e Escola.

Classe Aluno: Deve conter os seguintes atributos:
	nome: Representa o nome do aluno.
	idade: Representa a idade do aluno.
	Método mostrar_info(): Deve imprimir as informações do aluno.

Classe Escola: Deve conter os seguintes atributos:
	alunos: Um array ou lista para armazenar os objetos da classe Aluno.
	capacidade: Representa a capacidade máxima de alunos que a escola pode ter.
	Método adicionar_aluno(aluno): Deve adicionar um aluno à escola, considerando a capacidade.
	Método mostrar_alunos(): Deve imprimir as informações de todos os alunos da escola.

Crie um programa que instancie alguns alunos e uma escola e utilize seus métodos para adicionar os alunos e mostrar as informações.
'''
class Aluno:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def mostrar_info(self):
        print(f"Nome: {self.nome}")
        print(f"Idade: {self.idade}")

class Escola:
    def __init__(self, capacidade):
        self.alunos = []
        self.capacidade = capacidade

    def adicionar_aluno(self, aluno):
        if len(self.alunos) < self.capacidade:
            self.alunos.append(aluno)
        else:
            print("A escola está cheia!")

    def mostrar_alunos(self):
        for aluno in self.alunos:
            aluno.mostrar_info()
            print()

if __name__ == "__main__":
    a1 = Aluno("João", 15)
    a2 = Aluno("Maria", 16)
    a3 = Aluno("José", 17)

    e1 = Escola(2)
    e1.adicionar_aluno(a1)
    e1.adicionar_aluno(a2)
    e1.adicionar_aluno(a3)
    e1.mostrar_alunos()