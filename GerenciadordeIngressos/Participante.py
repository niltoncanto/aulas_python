class Participante:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email
        self.ingressos_comprados = []

    def getNome(self):
        return self._nome

    def setNome(self, nome):
        self._nome = nome

    def getEmail(self):
        return self._email

    def setEmail(self, email):
        self._email = email

    def comprar_ingresso(self, ingresso):
        self.ingressos_comprados.append(ingresso)

    def cancelar_ingresso(self, ingresso):
        ingresso.cancelar()
