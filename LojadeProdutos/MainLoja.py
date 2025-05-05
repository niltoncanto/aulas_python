class Produto:
    def __init__(self, nome, preco, qtdEstoque):
        self.nome = nome
        self.preco = preco
        self.qtdEstoque = qtdEstoque

    def comprar(self, quantidade):
        if self.qtdEstoque >= quantidade:
            self.qtdEstoque -= quantidade
        else:
            print("Quantidade insuficiente em estoque.")

    def reporEstoque(self, quantidade):
        self.qtdEstoque += quantidade

    def mostrarInfo(self):
        print("Nome:", self.nome)
        print("Preço:", self.preco)
        print("Quantidade em Estoque:", self.qtdEstoque)
        print("----------")


class Loja:
    def __init__(self):
        self.listaProdutos = []

    def adicionarProduto(self, produto):
        self.listaProdutos.append(produto)

    def mostrarProdutos(self):
        for produto in self.listaProdutos:
            produto.mostrarInfo()


# Demonstração de uso
if __name__ == "__main__":
    p1 = Produto("Celular", 1500.50, 10)
    p2 = Produto("Notebook", 3200.00, 5)

    minhaLoja = Loja()
    minhaLoja.adicionarProduto(p1)
    minhaLoja.adicionarProduto(p2)
    minhaLoja.mostrarProdutos()

    p1.comprar(2)
    p2.reporEstoque(3)
    minhaLoja.mostrarProdutos()
'''
Em Python, as convenções de nomenclatura são um pouco diferentes. Usamos "snake_case" para nomes de variáveis, métodos e funções, e "CamelCase" para nomes de classes. Não há regras rígidas sobre o nome do arquivo em relação às classes definidas nele, e você pode ter várias classes em um único arquivo. Também não há modificador explícito de acesso (como "private" ou "public") em Python; em vez disso, um sublinhado no início do nome de um atributo ou método indica que ele é "protegido" e não deve ser acessado diretamente.
'''