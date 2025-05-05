from abc import ABC, abstractmethod

class ServicoPetshop(ABC):
    def __init__(self, descricao, preco):
        self._descricao = descricao
        self._preco = preco

    @abstractmethod
    def exibir_informacoes(self):
        pass

    # Implemente os getters e setters para descricao e preco

# Crie as classes BanhoETosa, ConsultaVeterinaria e Hospedagem, herdando de ServicoPetshop

class BanhoETosa(ServicoPetshop):
    def __init__(self, descricao, preco, tamanho):
        super().__init__(descricao, preco)
        self._tamanho = tamanho  # P, M ou G

    def exibir_informacoes(self):
        print(f"Serviço: Banho e Tosa, Descrição: {self._descricao}, Preço: R${self._preco}, Tamanho: {self._tamanho}")

    # Implemente o getter e setter para tamanho
class Pet:
    def __init__(self, nome, especie):
        self._nome = nome
        self._especie = especie

    # Implemente os getters e setters aqui

class Agendamento:
    def __init__(self, pet, servico, data, horario):
        self._pet = pet  # Objeto da classe Pet
        self._servico = servico  # Objeto da classe ServicoPetshop ou subclasses
        self._data = data
        self._horario = horario

    def exibir_informacoes_agendamento(self):
        print(f"Agendamento para {self._pet._nome}, Espécie: {self._pet._especie}, Serviço: {type(self._servico).__name__}, Data: {self._data}, Horário: {self._horario}")
        self._servico.exibir_informacoes()

    # Implemente os getters e setters aqui
