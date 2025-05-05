'''
CLASSE PARTICIPANTE: Esta classe é responsável por gerenciar os participantes e seus ingressos comprados.
ATRIBUTOS:
- nome: Representa o nome do participante.
- email: Armazena o email do participante.
- ingressosComprados: Guarda os ingressos comprados por esse participante.

MÉTODOS:
- __init__(nome, email): contrutor inicializa o participante com os valores fornecidos.
- comprarIngresso(self, evento): recebe o participante(self) e o evento, intancia o Ingresso e inclui na lista do usuário 
- mostrarIngressos: Lista os ingressos do participante.
'''
from Ingresso import Ingresso


class Participante:
    def __init__(self, nome,email):
        self.nome = nome
        self.email = email
        self.ingressosComprados = []
    
    def comprarIngresso(self, evento):
        ingresso = Ingresso(self, evento)
        self.ingressosComprados.append(ingresso)
    
    def cancelar_ingresso(self, ingresso):
        ingresso.cancelar()

    def mostrarIngressosParticipantes(self):
        for ingresso in self.ingressosComprados:
            print(f"{ingresso.participante.nome} | Nome:{ingresso.evento.nomeEvento} | data:{ingresso.evento.localEvento} |data:{ingresso.evento.dataEvento} | data:{ingresso.getStatusIngresso()}")