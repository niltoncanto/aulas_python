def busca_binaria_recursiva(lista, item, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1

    if inicio > fim:
        return None  # O item não está na lista

    meio = (inicio + fim) // 2
    chute = lista[meio]

    if chute == item:
        return meio
    elif chute > item:
        return busca_binaria_recursiva(lista, item, inicio, meio - 1)
    else:
        return busca_binaria_recursiva(lista, item, meio + 1, fim)

# Exemplo de uso
minha_lista = [1, 3, 5, 7, 9]

# Testando a busca binária recursiva
print(busca_binaria_recursiva(minha_lista, 3))  # Deve retornar o índice 1
print(busca_binaria_recursiva(minha_lista, -1)) # Deve retornar None
