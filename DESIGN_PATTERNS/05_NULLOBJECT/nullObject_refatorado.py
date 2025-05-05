class Cliente:
    def __init__(self, nome, email):
        self.nome = nome
        self.email = email

    def enviar_email(self, mensagem):
        print(f"Enviando email para {self.email}: {mensagem}")

# Subclasse para representar o objeto nulo
class ClienteNulo(Cliente):
    def __init__(self):
        super().__init__("Cliente desconhecido", None)

    def enviar_email(self, mensagem):
        print("Nenhum cliente encontrado. Não foi possível enviar a notificação.")

    def is_null(self):
        return True


# Atualiza a lógica de busca para retornar um objeto nulo em vez de None
def buscar_cliente(id):
    if id == 1:
        return Cliente("João", "joao@example.com")
    else:
        return ClienteNulo()


# Remove verificações explícitas de `null` e usa polimorfismo
def notificar_cliente(id, mensagem):
    cliente = buscar_cliente(id)
    cliente.enviar_email(mensagem)

# Testes
notificar_cliente(1, "Bem-vindo ao sistema!")  # Deve enviar email
notificar_cliente(2, "Bem-vindo ao sistema!")  # Deve imprimir "Nenhum cliente encontrado. Não foi possível enviar a notificação."
