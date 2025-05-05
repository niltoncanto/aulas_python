def somaimpares(a,b):
    soma = 0
    if b<a:
        a,b = b,a
    
    for i in range(a+1,b):
        if i%2!=0:
            soma +=i
    return soma

a = int(input())
b = int(input())
print(somaimpares(a,b))
