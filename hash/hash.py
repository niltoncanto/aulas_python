def simple_hash(s):
    """ Uma função de hash muito simples para strings. """
    return sum(ord(char) for char in s)

def hash_index(s, table_size):
    """ Calcula o índice para uma string em uma tabela hash de tamanho table_size. """
    hash_value = simple_hash(s)
    return hash_value % table_size

# Exemplo com a string "hello" e uma tabela hash de tamanho 10
string = "hello"
table_size = 7
index = hash_index(string, table_size)

print("indice =", index)  # Índice onde "hello" seria armazenado na tabela hash

lista = ['Calcula','índice','para','uma','string','em','tabela']
indices = []
for s in lista:
    print(s)
    indices.append(hash_index(s, table_size))

print(indices)


def djb2(s, table_size):
    hash = 5381
    for char in s:
        hash = (hash * 33) + ord(char)
    return hash % table_size

# Exemplo com a string "hello" e uma tabela hash de tamanho 100
string = "hello"
table_size = 100
index = djb2(string, table_size)

print(index)
