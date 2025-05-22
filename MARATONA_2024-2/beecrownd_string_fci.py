def contar_frequencia(s):
    frequencias = {}  # Dicionário para armazenar a frequência de cada caractere
    for char in s:
        if char in frequencias:
            frequencias[char] += 1
        else:
            frequencias[char] = 1
    return frequencias

def ordena_frequencias(f):
  f = dict(sorted(f.items(),key=lambda item: (item[1], -ord(item[0]))))
  return f

entradas = []
try:
    while True:
        entradas.append(input())
except EOFError:
    pass


for i, s in enumerate(entradas):
  f = contar_frequencia(s)
  f = ordena_frequencias(f)
  for k,v in f.items():
    print(ord(k),v)
  if i<len(entradas)-1:
     print()