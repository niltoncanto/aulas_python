class Usuario:
    def __init__(self,nome,email):
        self.nome = nome
        self.email = email
    @property
    def nome(self): 
        return self.__nome
    @nome.setter
    def nome(self,nome):
        self.__nome = nome
    @nome.deleter
    def nome(self):
        del self.__nome
    #teste de propriedade
usuario = Usuario("joão","joao@gmail.com")
print(usuario.nome) #usando o getter
usuario.nome = "Maria" #usando o setter
print(usuario.nome) #usando o getter
del usuario.nome #usando o deleter
