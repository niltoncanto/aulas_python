def meu_decorador(func):          # 1️ recebe a função original
    def wrapper(*args, **kwargs): # 2️ função interna que adiciona lógica extra
        # Código antes
        resultado = func(*args, **kwargs)
        # Código depois
        return resultado
    return wrapper                # 3️ retorna a nova função decorada











