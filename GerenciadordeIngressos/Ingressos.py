from datetime import datetime

class Ingresso:
    def __init__(self, participante, evento):
        self.participante = participante
        self.evento = evento
        self.data_compra = datetime.now()
        self.cancelado = False

    def cancelar(self):
        self.cancelado = True