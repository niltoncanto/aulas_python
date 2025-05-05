from datetime import date

class Evento:
    def __init__(self, nome, local, data, capacidade_maxima):
        self.nome = nome
        self.local = local
        self.data = data
        self.capacidade_maxima = capacidade_maxima
        self.ingressos = []

    def criar_ingresso(self, participante):
        if len(self.ingressos) < self.capacidade_maxima:
            ingresso = Ingresso(participante, self)
            self.ingressos.append(ingresso)
            participante.comprar_ingresso(ingresso)
            return True
        return False

    def cancelar_ingresso(self, ingresso):
        ingresso.cancelar()
