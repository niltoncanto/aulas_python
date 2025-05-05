class Veiculo:
    total_veiculos = 0  # Variável de classe para contar o total de veículos cadastrados

    def __init__(self, marca, modelo, ano, preco):
        pass

class VeiculoNovo(Veiculo):
    def __init__(self, marca, modelo, ano, preco, garantia_anos):
        pass

class VeiculoUsado(Veiculo):
    def __init__(self, marca, modelo, ano, preco, quilometragem, unico_dono):
        pass

class Concessionaria:
    def __init__(self):
        pass

    def cadastrar_veiculo(self, veiculo):
        pass

    def registrar_venda(self, chave):
        pass

    def exibir_estoque(self):
        pass

    def exibir_vendas(self):
        pass

# Exemplo de uso
concessionaria = Concessionaria()
concessionaria.cadastrar_veiculo(VeiculoNovo("Toyota", "Corolla", 2021, 90000, 3))
concessionaria.cadastrar_veiculo(VeiculoUsado("Fiat", "Uno", 2010, 15000, 120000, True))

concessionaria.exibir_estoque()
concessionaria.registrar_venda(("Toyota", "Corolla", 2021))
concessionaria.exibir_vendas()

print(f"Total de veículos cadastrados: {Veiculo.total_veiculos}")
