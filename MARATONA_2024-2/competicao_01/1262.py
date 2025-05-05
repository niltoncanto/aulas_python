import math
def calcula_ciclos(historico,num_processos):
  ciclos = 0
  i = 0
  while i<len(historico):
    if historico[i] == 'W':
      ciclos += 1
      i += 1
    else:
      ciclos +=1
      j = 0
      while i<len(historico) and j<num_processos and historico[i]=="R":
        i+=1
        j+=1

  return ciclos

x = calcula_ciclos("WWWWW",5)
print(x)