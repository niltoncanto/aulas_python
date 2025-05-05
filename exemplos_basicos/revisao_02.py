# 1. Início: O fluxograma começa aqui.
# 2. Menu: Adicionar Tarefa, Visualizar Tarefas, Remover Tarefa, Sair.
# 3. Decisão: O programa verifica qual opção o usuário escolheu.
#    - Se o usuário escolheu 'Adicionar Tarefa':
#      	1. O programa pede ao usuário para inserir a descrição da tarefa.
#      	2. A tarefa é adicionada ao dicionário de tarefas.
#      	3. O programa retorna ao Menu.
#    - Se o usuário escolheu 'Visualizar Tarefas':
#      	1. O programa verifica se há tarefas no dicionário.
#      	2. Se houver, o programa imprime todas as tarefas.
#      	3. O programa retorna ao Menu.
#    - Se o usuário escolheu 'Remover Tarefa':
#      	1. O programa pede ao usuário para inserir o ID da tarefa a ser removida.
#      	2. O programa verifica se o ID fornecido existe no dicionário.
#      	3. Se existir, a tarefa é removida do dicionário.
#      	4. O programa retorna ao Menu.
#    - Se o usuário escolheu 'Sair':
#      	1. O programa termina.
# 4. Fim: O fluxograma termina aqui.
import time
lista_tarefas = {}
id_tarefa = 0
def menu():
    while True:
        print("**** Menu ******")
        print("1. Adicionar Tarefa")
        print("2. Listar Tarefas")
        print("3. Excluir Tarefas")
        print("4. Sair")
        print("*****************")
        opcao = int(input("Entre com usa opção: "))
        if opcao<1 and opcao>4:
            print("Opção inválida, tente novamente!")
            continue
        tarefas(opcao)


def tarefas(opcao):
    global id_tarefa
    match opcao:
        case 1:
            descricao_tarefa = input("Entre com a descricao da tarefa: ")
            lista_tarefas[id_tarefa] = descricao_tarefa
            id_tarefa += 1
        case 2:
            if len(lista_tarefas)==0:
                print("Lista de Tarefas vazia!")
            else:
                for k,v in lista_tarefas.items():
                    print(f"ID:{k} Descrição:{v}")
        case 3:
            id_delete = int(input("Informe o id da tarefa a ser excluída: "))
            if lista_tarefas.get(id_delete):
                removido = lista_tarefas.pop(id_delete)
                print(f"Tarefa \"{removido}\" foi removida com sucesso!")
        case 4:
            print("Saindo do sistema...")
            time.sleep(1)
            exit()
    menu()

menu()

    
