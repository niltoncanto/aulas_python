def contador(maximo):
    i = 0
    while i < maximo:
        #yield i pausa a função e retorna o valor atual de i.
        val = yield i
        # Se um valor for enviado com .send(), ele substitui o contador i
        if val is not None:
            i = val
        #Se nenhum valor for enviado, o contador simplesmente incrementa i.
        else:
            i += 1
gen = contador(10)
print(next(gen))    # 0
print(next(gen))    # 1
print(gen.send(5))  # muda i para 5
print(next(gen))    # 6









