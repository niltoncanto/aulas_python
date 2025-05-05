import math
def porcentagem(a,b):
    total_placas = a*b
    taxa = 0
    valores = ''
    for i in range(1,10):
        taxa = i*0.1
        valor = total_placas*taxa
        valores += str(math.ceil(round(valor,5))) + ' '
        #print(i,a,b,total_placas,taxa,valor,math.ceil(round(valor,5)))
    return valores

entrada = input()
partes = entrada.split()
a = int(partes[0])
b = int(partes[1])
r = porcentagem(a,b)
print(r.strip())