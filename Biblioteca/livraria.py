livros = []
emprestimos = {}

while True:
    print("1. Adicionar livro")
    print("2. Listar livros")
    print("3. Emprestar livro")
    print("4. Ver empréstimos")
    print("0. Sair")
    opcao = int(input("Escolha uma opção: "))

    if opcao == 1:
        titulo = input("Digite o título do livro: ")
        livros.append(titulo)
    elif opcao == 2:
        print("Livros:")
        for livro in livros:
            print(livro)
    elif opcao == 3:
        titulo_emprestimo = input("Digite o título para emprestar: ")
        if titulo_emprestimo not in emprestimos:
            leitor = input("Digite o nome do leitor: ")
            emprestimos[titulo_emprestimo] = leitor
        else:
            print("Livro já emprestado!")
    elif opcao == 4:
        print("Empréstimos:")
        for livro, leitor in emprestimos.items():
            print("Livro:", livro, "- Leitor:", leitor)
    elif opcao == 0:
        print("Saindo...")
        break
    else:
        print("Opção inválida!")