musica = {
    0:'PROXYCITY',
    1:'P.Y.N.G.',
    2:'DNSUEY!',
    3:'SERVERS',
    4:'HOST!',
    5:'CRIPTONIZE',
    6:'OFFLINE DAY',
    7:'SALT',
    8:'ANSWER!',
    9:'RAR?',
    10:'WIFI ANTENNAS',
}
c = int(input())
listax = []
listay = []
for i in range(c):
    #listax.append(int(input()))
    #listay.append(int(input()))
    # Lê a entrada do usuário como uma string, separa por espaço e converte para inteiros
    x, y = map(int, input().split())
    listax.append(x)
    listay.append(y)

for i in range(c):
    x = listax[i]
    y = listay[i]
    print(musica.get(x+y))