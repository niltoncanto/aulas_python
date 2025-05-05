'''
CLASSE INGRESSO: Esta classe é responsável por gerenciar os ingressos associados a participantes e eventos.
ATRIBUTOS:
- participante: Representa o participante que comprou o ingresso.
- evento: Indica o evento associado ao ingresso.
- dataCompra: Armazena a data e a hora da compra do ingresso.
- statusIngresso: Indica se o ingresso ainda é válido ou foi cancelado.
MÉTODOS:
- __init__(participante, evento): Construtor cria um ingresso associado ao participante e evento fornecidos, adiciona o ingresso à lista de ingressos do participante e à lista de inscritos do evento.
'''
from datetime import datetime

class Ingresso:
    def __init__(self,participante,evento):
        self.participante = participante
        self.evento = evento
        self.dataCompra = datetime.now()
        self.statusIngresso = True
        evento.incluirInscrito(self)

    def cancelar(self):
        self.statusIngresso = False

    def getStatusIngresso(self):
        return self.statusIngresso
    def setStatusIngresso(self,status):
        self.statusIngresso = status
    