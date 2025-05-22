def validar_cpf(cpf: str) -> bool:
    if not cpf.isdigit() or len(cpf) != 11:
        return False
    
    if cpf == cpf[0] * 11:
        return False  # Rejeita CPFs com dígitos iguais
    
    # Cálculo do primeiro dígito verificador
    soma = sum(int(cpf[i]) * (10 - i) for i in range(9))
    dig1 = (soma * 10 % 11) % 10
    
    # Cálculo do segundo dígito verificador
    soma = sum(int(cpf[i]) * (11 - i) for i in range(10))
    dig2 = (soma * 10 % 11) % 10
    return cpf[-2:] == f"{dig1}{dig2}"






