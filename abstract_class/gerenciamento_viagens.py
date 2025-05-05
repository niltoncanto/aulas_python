from abc import ABC, abstractmethod

# Classe Abstrata Viagem
class Viagem(ABC):
    def __init__(self, destino, duracao, preco_base):
        self.destino = destino
        self.duracao = duracao
        self.preco_base = preco_base
    
    @abstractmethod
    def calcular_preco_total(self):
        pass

# Subclasse Cruzeiro
class Cruzeiro(Viagem):
    def __init__(self, destino, duracao, preco_base, taxa_servico):
        super().__init__(destino, duracao, preco_base)
        self.taxa_servico = taxa_servico
    
    def calcular_preco_total(self):
        return self.preco_base + self.taxa_servico

# Subclasse Viagem Terrestre
class ViagemTerrestre(Viagem):
    def __init__(self, destino, duracao, preco_base, custo_guia):
        super().__init__(destino, duracao, preco_base)
        self.custo_guia = custo_guia
    
    def calcular_preco_total(self):
        return self.preco_base + self.custo_guia

# Subclasse Viagem Aérea
class ViagemAerea(Viagem):
    def __init__(self, destino, duracao, preco_base, taxa_bagagem):
        super().__init__(destino, duracao, preco_base)
        self.taxa_bagagem = taxa_bagagem
    
    def calcular_preco_total(self):
        return self.preco_base + self.taxa_bagagem

# Classe AgenciaViagens
class AgenciaViagens:
    def __init__(self):
        self.viagens = []
    
    def adicionar_viagem(self, viagem):
        self.viagens.append(viagem)
    
    def calcular_receita_total(self):
        total = 0
        for viagem in self.viagens:
            total += viagem.calcular_preco_total()
        return total
    
    def exibir_detalhes_viagem(self):
        for viagem in self.viagens:
            print(f"Destino: {viagem.destino}, Duração: {viagem.duracao} dias, Preço Total: {viagem.calcular_preco_total()}")

# Exemplo de Uso
agencia = AgenciaViagens()

cruzeiro = Cruzeiro("Bahamas", 7, 5000, 1000)
terrestre = ViagemTerrestre("Chile", 10, 3000, 500)
aerea = ViagemAerea("Japão", 15, 8000, 200)

agencia.adicionar_viagem(cruzeiro)
agencia.adicionar_viagem(terrestre)
agencia.adicionar_viagem(aerea)

agencia.exibir_detalhes_viagem()
print(f"Receita Total: R$ {agencia.calcular_receita_total()}")
