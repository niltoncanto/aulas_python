#dicionários python

dic = {} #dicionário vazio
dic = {
    "nome":"José",
    "idade":50,
    "profissão":"Engenheiro",
    "endereço":{"Rua":"Maria Antonia",
                "Número":50,
                "cep":'024500006'
                }
}

print(dic["nome"])
print(dic["profissão"])
print(dic["endereço"]["Número"])
dic['cpf']="09505567855"
print(dic['cpf'])

del dic["cpf"]
print(dic)

for k in dic.keys():
    print(k)

for v in dic.values():
    print(v)

for v in dic.values():
    if isinstance(v,dict):
        for v1 in v.values():
            print(v1)

print(dic.get('nome1'),"chave não encontrada")
dic.setdefault