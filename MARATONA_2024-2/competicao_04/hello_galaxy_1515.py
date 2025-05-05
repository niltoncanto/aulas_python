while True:
  n = int(input())
  if n==0:
    break
  mensagens = []
  for i in range(n):
    mensagens.append(list(map(str,input().split())))
  civilizacao_mais_antiga = ''
  ano_mais_antigo = 2114
  for planeta,ano_recebido,tempo_envio in mensagens:
      ano_envio = int(ano_recebido) - int(tempo_envio)
      if ano_envio<ano_mais_antigo:
        ano_mais_antigo = ano_envio
        civilizacao_mais_antiga = planeta
  print(civilizacao_mais_antiga)