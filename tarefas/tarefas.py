import time

tarefas = {}
id_tarefa = 1
while True:
    print("\n")
    print("Agendador de Tarefas")
    print("\n")
    print("1 - Adicionar Tarefas ")
    print("2 - Visualizar Tarefas")
    print("3 - Excluir Tarefas")
    print("4 - Sair")
    print("\n")
    try:
        opcao = int(input("Digite a opção desejada: "))
    except ValueError:
        print("Opção inválida ...")
        input("Pressione ENTER para continuar ...")
        continue
    print("\n")

    if opcao==1:
        #inserir tarefas no dicionario
        dsc_tarefa = input("Digite a descrição da tarefa: ")
        tarefas[id_tarefa] = dsc_tarefa
        print("Tarefa adicionada com sucesso ...")
        print(f"{id_tarefa} => {tarefas[id_tarefa]}")
        id_tarefa += 1
    elif opcao==2:
        #visualizar tarefas
        if len(tarefas)==0:
            print("Nenhuma tarefa cadastrada ...")
        else:
            print("Lista de tarefas cadastradas ...")
            for id, dsc in tarefas.items():
                print(id, dsc)
    elif opcao==3:
        #excluir tarefas
        id_tarefa = int(input("Digite o id da tarefa a ser excluída: "))
        if id_tarefa in tarefas:
            del tarefas[id_tarefa]
            print("Tarefa excluída com sucesso ...")
        else:
            print("Tarefa não encontrada ...")
    elif opcao==4:
        #sair
        print("Saindo do programa ...")
        time.sleep(2)
        break
    else:
        print("Opção inválida ...")
    print("\n")
    input("Pressione ENTER para continuar ...")