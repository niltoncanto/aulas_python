tarefas = {}
contador_tarefas = 1

while True:
    print("\nGerenciador de Tarefas")
    print("1 - Adicionar Tarefa")
    print("2 - Visualizar Tarefas")
    print("3 - Remover Tarefa")
    print("4 - Sair")
    
    opcao = input("Escolha uma opção: ")
    
    if opcao == '1':
        descricao = input("\nDigite a descrição da tarefa: ")
        tarefas[contador_tarefas] = descricao
        contador_tarefas += 1
        print("Tarefa adicionada com sucesso!")
        
    elif opcao == '2':
        if not tarefas:
            print("\nNenhuma tarefa encontrada.")
        else:
            print("\nTarefas:")
            for id, descricao in tarefas.items():
                print(f"ID: {id}, Descrição: {descricao}")
                
    elif opcao == '3':
        id = int(input("\nDigite o ID da tarefa que deseja remover: "))
        if id not in tarefas:
            print("Tarefa não encontrada.")
        else:
            del tarefas[id]
            print("Tarefa removida com sucesso!")
            
    elif opcao == '4':
        print("Encerrando o programa...")
        break

    else:
        print("\nOpção inválida. Tente novamente.")




    
