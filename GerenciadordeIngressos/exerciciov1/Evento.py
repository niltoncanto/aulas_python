'''
OBJETIVO: Desenvolver um sistema para gerenciar eventos e a compra de ingressos por participantes.
CLASSE EVENTO: Esta classe é responsável por criar e gerenciar os eventos disponíveis.
ATRIBUTOS:
- nomeEvento: Representa o nome do evento.
- localEvento: Indica o local onde o evento ocorrerá.
- dataEvento: Armazena a data do evento.
- capacidadeEvento: Indica a capacidade máxima de pessoas que podem participar do evento.
- inscritosEvento: Guarda os ingressos associados a esse evento.
- eventos: Estático, guarda todos os eventos criados.
MÉTODOS:
- Evento(nomeEvento, localEvento, dataEvento, capacidadeEvento): Inicializa o evento com os valores fornecidos e adiciona o evento à lista estática eventos.
- getEventos(): Retorna a lista estática de todos os eventos cadastrados.
- mostraInfoEvento: Lista os dados do evento.
- cancelarEvento(): Cancela o evento, definindo o status de todos os ingressos associados a ele como inválido e remove o evento da lista estática eventos.
- incluirInscrito(): inclui inscrito na lista inscritosEvento.
'''

class Evento:
    eventos=[]
    def __init__(self,nomeEvento,localEvento,dataEvento,capacidadeEvento):
        self.nomeEvento = nomeEvento
        self.localEvento = localEvento
        self.dataEvento = dataEvento
        self.capacidadeEvento = capacidadeEvento
        self.inscritosEvento = []
        Evento.eventos.append(self)

    def getEvento(nomeEvento,localEvento,dataEvento, capacidadeEvento):
        return Evento.eventos
    
    def mostrarInfoEvento(self):
        print("Informações do Evento")
        print(f"Nome:{self.nomeEvento} - Local:{self.localEvento} - Data:{self.dataEvento} - Capacidade:{self.capacidadeEvento}")

    def cancelarEvento(self):
        for ingresso in self.inscritosEvento:
            ingresso.setStatusIngresso(False)
        Evento.eventos.remove(self)
        print("Evento Cancelado")
    
    def incluirInscrito(self,ingresso):
        self.inscritosEvento.append(ingresso)

    def getNomeEvento(self):
        return self.nomeEvento
    
    def setNomeEvento(self,nomeEvento):
        self.nomeEvento = nomeEvento

    def getDataEvento(self):
        return self.dataEvento

    def setDataEvento(self,dataEvento):
        self.dataEvento = dataEvento
    
    def getCapacidadeEvento(self):
        return self.capacidadeEvento
    
    def setCapacidadeEvento(self,capacidadeEvento):
        self.capacidadeEvento = capacidadeEvento

    def getInscritosEvento(self):
        return self.inscritosEvento
