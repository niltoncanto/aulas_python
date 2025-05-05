class A:
    def mostrar(self):
        print("Classe A")

class B(A):
    def mostrar(self):
        print("Classe B")

obj = B()
obj.mostrar()