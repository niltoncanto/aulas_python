class Produto:

    def calcularPreco(self) -> int:
        return self.preco

    def calcularPreco(self, quantidade: int) -> float:
        return self.preco * quantidade

if __name__=="__main__":
    produto = Produto()
    produto.preco = 10
    print(produto.calcularPreco())
    print(produto.calcularPreco(2))

# Path: python_aulas/Polimorfismo/teste.py