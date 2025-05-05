def print_type(data):
    match data:
        case int() if data > 10:  
            print(f"Inteiro maior que 10: {data}")
        case bool() if data is True:  
            print("Booleano: True")
        case str() if data.strip():  
            print(f"String não vazia: {data}")
        case _:
            print("Tipo não suportado")



            