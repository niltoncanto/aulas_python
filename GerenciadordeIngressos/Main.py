from datetime import date
from participante import Participante
from ingresso import Ingresso
from evento import Evento

# Criando alguns participantes
participante1 = Participante("Alice", "alice@example.com")
participante2 = Participante("Bob", "bob@example.com")

# Criando um evento
evento1 = Evento("Concerto Musical", "Teatro Principal", date(2023, 8, 30), 100)

# Comprando ingressos
ingresso_criado1 = evento1.criar_ingresso(participante1)
ingresso_criado2 = evento1.criar_ingresso(participante2)

print("Ingresso de Alice criado:", ingresso_criado1)
print("Ingresso de Bob criado:", ingresso_criado2)

# Cancelando o ingresso de um participante
ingresso_cancelado = participante1.ingressos_comprados[0]
evento1.cancelar_ingresso(ingresso_cancelado)

print("Ingresso de Alice cancelado:", ingresso_cancelado.cancelado)
