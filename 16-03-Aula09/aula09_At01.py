'''
    Descobrir a quantidade de paginas disponiveis
        Percorrer todas as paginas
            Todos os produtos
    Pegar o nome dos produtos
    Pegar o nome do produto
    Pegar o valor do produtoPegar o fabricante
    Pegar a % do desconto do produto
    Salvar o arquivos em xlsx
'''
from bs4 import BeautifulSoup
import requests

def ConsultarQuantidadePagina(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        print('oie')

url = 'https://www.superpaguemenos.com.br/hortifruti/'
ConsultarQuantidadePagina(url)

