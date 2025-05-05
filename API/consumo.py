import requests

# URL da API do GitHub
url = 'https://api.github.com/repositories'

# Fazendo uma solicitação GET
response = requests.get(url)

# Verificando o status da resposta
if response.status_code == 200:
    data = response.json()
    for repo in data:
        print(f"Nome do repositório: {repo['name']}")
        print(f"Dono: {repo['owner']['login']}")
        print(f"URL: {repo['html_url']}")
        print("---")
else:
    print("Não foi possível acessar a API.")
