class Veiculo:
    total_veiculos = 0  # Variável de classe para contar o total de veículos cadastrados
    def __init__(self, marca, modelo, ano, preco):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.preco = preco
        Veiculo.total_veiculos += 1  # Incrementa o total de veículos a cada instância criada

class VeiculoNovo(Veiculo):
    def __init__(self, marca, modelo, ano, preco, garantia_anos):
        self.garantia_anos = garantia_anos
        super().__init__(marca, modelo, ano, preco)

class VeiculoUsado(Veiculo):
    def __init__(self, marca, modelo, ano, preco, quilometragem, unico_dono):
        self.quilometragem = quilometragem
        self.unico_dono = unico_dono
        super().__init__(marca, modelo, ano, preco)

class Concessionaria:
    def __init__(self):
        self.veiculos = {}  # Dicionário para armazenar os veículos disponíveis
        self.vendas = []  # Lista para armazenar os veículos vendidos

    def cadastrar_veiculo(self, veiculo):
        chave = (veiculo.marca, veiculo.modelo, veiculo.ano)
        self.veiculos[chave] = veiculo

    def registrar_venda(self, chave):
        if chave in self.veiculos:
            veiculo_vendido = self.veiculos.pop(chave)
            self.vendas.append(veiculo_vendido)
            Veiculo.total_veiculos -= 1
            return f"Venda registrada: {veiculo_vendido.marca} {veiculo_vendido.modelo}, {veiculo_vendido.ano}"
        else:
            return "Veículo não encontrado no estoque."

    def exibir_estoque(self):
        print("Estoque de Veículos:")
        for chave, veiculo in self.veiculos.items():
            return f"{veiculo.marca} {veiculo.modelo}, Ano: {veiculo.ano}, Preço: {veiculo.preco}"

    def exibir_vendas(self):
        print("Veículos Vendidos:")
        for veiculo in self.vendas:
            return f"{veiculo.marca} {veiculo.modelo}, Ano: {veiculo.ano}, Preço: {veiculo.preco}"

    def buscar_por_marca(self, marca):
        print(f"Veículos da marca {marca}:")
        encontrados = False
        for veiculo in self.veiculos.values():
            if veiculo.marca == marca:
                print(f"{veiculo.marca} {veiculo.modelo}, Ano: {veiculo.ano}, Preço: {veiculo.preco}")
                encontrados = True
        if not encontrados:
            return f"Nenhum veículo da marca {marca} encontrado no estoque."

# Exemplo de uso
concessionaria = Concessionaria()
concessionaria.cadastrar_veiculo(VeiculoNovo("Toyota", "Corolla", 2021, 90000, True))
concessionaria.cadastrar_veiculo(VeiculoUsado("Fiat", "Uno", 2010, 35000, 120000, True))
concessionaria.cadastrar_veiculo(VeiculoUsado("Fiat", "147", 1980, 15000, 150000, True))

print(concessionaria.exibir_estoque())
print(concessionaria.registrar_venda(("Toyota", "Corolla", 2021)))
print(concessionaria.exibir_estoque())
print(concessionaria.exibir_vendas())
concessionaria.buscar_por_marca("Fiat")
print(f"Total de veículos cadastrados: {Veiculo.total_veiculos}")

