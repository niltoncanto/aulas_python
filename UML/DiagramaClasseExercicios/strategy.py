from abc import ABC, abstractmethod

# Interface Voar
class Voar(ABC):
    @abstractmethod
    def voar(self):
        pass

# Classes concretas que implementam a interface Voar
class VoarDia(Voar):
    def voar(self):
        print("O avião está voando durante o dia.")

class VoarNoite(Voar):
    def voar(self):
        print("O avião está voando durante a noite.")

# Interface Pousar
class Pousar(ABC):
    @abstractmethod
    def pousar(self):
        pass

# Classes concretas que implementam a interface Pousar
class PousarDia(Pousar):
    def pousar(self):
        print("O avião está pousando durante o dia.")

class PousarNoite(Pousar):
    def pousar(self):
        print("O avião está pousando durante a noite.")

# Classe Aviao que usa as estratégias de Voar e Pousar
class Aviao:
    def __init__(self):
        self.voarForma = None
        self.pousarForma = None

    def setVoar(self, voarForma: Voar):
        self.voarForma = voarForma

    def setPousar(self, pousarForma: Pousar):
        self.pousarForma = pousarForma

    def performanceVoar(self):
        if self.voarForma:
            self.voarForma.voar()
        else:
            print("Nenhuma estratégia de voo definida.")

    def performancePousar(self):
        if self.pousarForma:
            self.pousarForma.pousar()
        else:
            print("Nenhuma estratégia de pouso definida.")

    def informarDados(self):
        print("Dados do avião informados.")

# Subclasse específica Boeing757
class Boeing757(Aviao):
    def informarDados(self):
        print("Este é um Boeing 757.")

# Simulador do Boeing 757
class SimuladorBoeing757:
    def main(self):
        # Criando um Boeing 757
        boeing = Boeing757()

        # Definindo comportamento de voo e pouso
        boeing.setVoar(VoarDia())
        boeing.setPousar(PousarNoite())

        # Executando as performances
        boeing.performanceVoar()  # O avião voa durante o dia
        boeing.performancePousar()  # O avião pousa à noite

        # Informando dados do avião
        boeing.informarDados()

# Execução do simulador
if __name__ == "__main__":
    simulador = SimuladorBoeing757()
    simulador.main()
