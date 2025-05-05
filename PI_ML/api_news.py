#pip install newsapi-python
'''from newsapi import NewsApiClient
# Init
newsapi = NewsApiClient(api_key='7903a5f0cdbe4df8a16d81fe2c04c169')
# /v2/top-headlines
top_headlines = newsapi.get_top_headlines(q='bitcoin',
                                          sources='bbc-news,the-verge',
                                          category='business',
                                          language='en',
                                          country='us')
# /v2/everything
all_articles = newsapi.get_everything(q='bitcoin',
                                      sources='bbc-news,the-verge',
                                      domains='bbc.co.uk,techcrunch.com',
                                      from_param='2017-12-01',
                                      to='2017-12-12',
                                      language='en',
                                      sort_by='relevancy',
                                      page=2)
# /v2/top-headlines/sources
sources = newsapi.get_sources()'''

import json  # Importa o módulo json para trabalhar com dados no formato JSON.
import requests  # Importa o módulo requests para fazer requisições HTTP.

apikey = '7903a5f0cdbe4df8a16d81fe2c04c169'  
keyword = 'ibm'  # Define o termo de pesquisa para a API.
url = f'https://newsapi.org/v2/everything?q={keyword}&apiKey={apikey}'  # Constrói a URL para a requisição API com a palavra-chave e a chave API.

response = requests.get(url)  # Faz uma requisição GET para a URL especificada e armazena a resposta.
#print(response)  # Imprime o objeto de resposta para verificação de status (não o conteúdo real).

data = response.json()  # Converte a resposta da API de JSON para um dicionário Python.
print(data)  # Imprime o dicionário de dados convertido.

# Verifica se o código de status da resposta é 200, indicando sucesso.
if response.status_code == 200:
    articles = data['articles']  # Extrai a lista de artigos da resposta JSON.
    with open("noticias_100424.json", 'w', encoding='utf-8') as f:  # Abre um arquivo para escrita em UTF-8.
        # Salva os artigos em um arquivo JSON formatado.
        json.dump(articles, f, ensure_ascii=False, indent=4)
else:
    print("erro ao acessar a api.")  # Imprime uma mensagem de erro se a API não retornar um status 200.

#print(articles)  # Imprime a lista de artigos extraídos.
print(len(articles))  # Imprime o número de artigos na lista.
print(articles[0].keys()) # Imprime as chaves do primeiro artigo.
print(articles[0])  # Imprime o primeiro artigo da lista.

