import time
from functools import wraps  # Importa wraps
# Nosso decorador
def log_exec_time(func):
    @wraps(func)  # Preserva metadata da função original
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        end = time.time()
        print(f"[{func.__name__}] Executado em {end - start:.4f} segundos.")
        return result
    return wrapper
# Aplicando o decorador com @
@log_exec_time
def processar_dados():
    time.sleep(2)
    print("Processamento concluído.")

processar_dados()