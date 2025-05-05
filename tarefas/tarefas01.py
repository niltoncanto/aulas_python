""" 1. Início: O fluxograma começa aqui.
2. Menu: Adicionar Tarefa, Visualizar Tarefas, Remover Tarefa, Sair.
3. Decisão: O programa verifica qual opção o usuário escolheu.
   - Se o usuário escolheu 'Adicionar Tarefa':
     	1. O programa pede ao usuário para inserir a descrição da tarefa.
     	2. A tarefa é adicionada ao dicionário de tarefas.
     	3. O programa retorna ao Menu.
   - Se o usuário escolheu 'Visualizar Tarefas':
     	1. O programa verifica se há tarefas no dicionário.
     	2. Se houver, o programa imprime todas as tarefas.
     	3. O programa retorna ao Menu.
   - Se o usuário escolheu 'Remover Tarefa':
     	1. O programa pede ao usuário para inserir o ID da tarefa a ser removida.
     	2. O programa verifica se o ID fornecido existe no dicionário.
     	3. Se existir, a tarefa é removida do dicionário.
     	4. O programa retorna ao Menu.
   - Se o usuário escolheu 'Sair':
     	1. O programa termina.
4. Fim: O fluxograma termina aqui. """
id_tarefa = 0
tarefas = {}

def menu():
    print('Menu')
    print('1. Adicionar Tarefa')
    print('2. Visualizar Tarefa')
    print('3. Remover Tarefa')
    print('4. Sair')
    escolha = int(input("Opção: "))
    return escolha

def agenda(opcao):
    global id_tarefa
    if opcao==1:
        descricao = input("Entre com a descrição da tarefa: ")
        tarefas[id_tarefa] = descricao

        id_tarefa+=1
    if opcao==2:
        if len(tarefas)==0:
            print("Não há tarefas")
        else:
            for i in tarefas:
                print(f"{i}:{tarefas[i]}")
    if opcao==3:
        apagar = int(input('informe o id da tarefa:'))
        if apagar in tarefas:
            del tarefas[apagar]
            print("tarefa removida com sucesso!")
        else:
            print('tarefa não encontrada')
    if opcao==4:
        return False

if __name__=="__main__":
    while True:
        opcao = menu()
        result = agenda(opcao)
        


