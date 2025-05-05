def pode_formar_triangulo(varetas):
    varetas.sort()
    if (varetas[0] + varetas[1] > varetas[2] or
        varetas[0] + varetas[2] > varetas[3] or
        varetas[1] + varetas[2] > varetas[3]):
        return 'S'
    else:
        return 'N'

a, b, c, d = map(int, input().split())
resultado = pode_formar_triangulo([a, b, c, d])
print(resultado)