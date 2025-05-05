# Inicializa um dicionário com as salas e seus respectivos status
salas = {"Sala A": "Disponível", "Sala B": "Disponível", "Sala C": "Disponível", "Sala D": "Disponível", "Sala E": "Disponível"}

while True:  # Início do loop principal
    try:
        # Mostra o menu de opções para o usuário
        print("\nMenu:")
        print("1. Listar salas disponíveis")
        print("2. Reservar uma sala")
        print("3. Cancelar reserva de uma sala")
        print("4. Sair")
        opcao = input("Digite sua opção: ")

        # Opção para listar as salas disponíveis
        if opcao == "1":
            for sala, status in salas.items():
                print(f"{sala} - {status}")
        # Opção para reservar uma sala
        elif opcao == "2":
            sala = input("Digite o nome da sala que deseja reservar: ")
            if sala in salas and salas[sala] == "Disponível":
                salas[sala] = "Reservada"
                print("Sala reservada com sucesso!")
            else:
                print("Sala não está disponível para reserva.")
        # Opção para cancelar a reserva de uma sala
        elif opcao == "3":
            sala = input("Digite o nome da sala cuja reserva deseja cancelar: ")
            if sala in salas and salas[sala] == "Reservada":
                salas[sala] = "Disponível"
                print("Reserva cancelada com sucesso!")
            else:
                print("Sala não está reservada.")
        # Opção para sair do programa
        elif opcao == "4":
            break
        else:
            print("Opção inválida!")
    except Exception as e:
        print(f"Erro: {e}")