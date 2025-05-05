'''
Inverter string: Escreva uma função que inverta uma string. Comentário: 
você pode usar funções nativas da linguagem escolhida ou implementar uma solução manual usando laços.
'''

def invertString(string):
    return string[::-1]

def invertString2(string):
    stringInvertida = ""
    for i in range(len(string)-1,-1,-1):
        stringInvertida += string[i]
    return stringInvertida

string = input("Digite uma string: ")
print(invertString(string))
print(invertString2(string))