# cadastro_refatorado.py

class Usuario:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def __str__(self):
        return f"{self.nome}, {self.idade} anos"


class Cadastro:
    def __init__(self):
        self.usuarios = []

    def adicionar_usuario(self, usuario):
        self.usuarios.append(usuario)

    def listar_usuarios(self):
        for usuario in self.usuarios:
            print(usuario)

    def salvar_usuario_em_arquivo(self, usuario, caminho="usuarios.txt"):
        with open(caminho, "a") as f:
            f.write(f"{usuario.nome},{usuario.idade}\n")
