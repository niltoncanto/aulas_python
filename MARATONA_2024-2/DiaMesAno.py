def tempo():
    dias = int(input("Entre com um número inteiro de dias:"))
    ano = dias//365
    mes = (dias%365)//30
    dias = (dias%365)%30
    return ano,mes,dias

print(tempo())
    