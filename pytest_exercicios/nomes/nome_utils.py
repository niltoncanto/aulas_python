
def normalizar_nome(nome: str) -> str:
    partes = nome.strip().split()
    return ' '.join(p.capitalize() for p in partes)
