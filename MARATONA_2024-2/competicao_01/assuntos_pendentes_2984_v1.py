# A dica para solução de problema passa pela criação de uma pilha, uma pilha é uma estrutura de dados do tipo LIFO Last In - First Out,
# ou seja, o último a entrar na pilha é o primeiro a sair, você pode simular uma pilha com uma lista em python.
# pilha = []
# pilha.append("(") #empilhando o caracter "(", o caracter é sempre inserido no final da lista (pilha)
# pilha.append("(") #empilhando o caracter "("
#pilha.pop()       #desempilhando o caracter "(" o pop retira sempre do final da lista (pilha)

# Inicializa uma lista vazia chamada 'pilha', que será usada para armazenar parênteses abertos
pilha = []

# Solicita ao usuário que digite um texto e o armazena na variável 'texto'
texto = input("Digite um texto: ")

# Itera sobre cada caractere no texto fornecido
for i in texto:
  # Se o caractere atual é um parêntese aberto "(",
  # ele é adicionado à pilha
  if i == "(":
    pilha.append(i)
  # Se o caractere atual não é um parêntese aberto mas a pilha não está vazia,
  # isso implica que podemos ter um parêntese para fechar,
  # então um parêntese aberto é removido da pilha
  elif len(pilha) > 0:
    pilha.pop()

# Após processar todo o texto, verifica-se se a pilha ainda contém parênteses abertos
if len(pilha) > 0:
  # Se a pilha não estiver vazia, isso significa que existem parênteses abertos
  # que não foram fechados. A quantidade de assuntos pendentes (parênteses abertos não fechados)
  # é informada ao usuário.
  print(f"Ainda temos {len(pilha)} assunto(s) pendente(s)!")
else:
  # Se a pilha estiver vazia, todos os parênteses abertos foram devidamente fechados,
  # indicando que o texto está balanceado. Uma mensagem correspondente é exibida.
  print("Partiu RU!")