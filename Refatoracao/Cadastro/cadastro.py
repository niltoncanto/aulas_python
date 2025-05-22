# cadastro.py

class A:
    def __init__(self):
        self.d = []

    def b(self, u):
        self.d.append(u)

    def c(self):
        for u in self.d:
            print(u["n"])
            print(u["i"])
            print("Usuário salvo!")

    def s(self, nome, idade):
        u = {"n": nome, "i": idade}
        self.b(u)
        with open("usuarios.txt", "a") as f:
            f.write(nome + "," + str(idade) + "\n")
