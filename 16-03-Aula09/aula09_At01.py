'''
    Descobrir a quantidade de paginas disponiveis -> OK
        Percorrer todas as paginas -> OK
            Todos os produtos

    Pegar o nome dos produtos -> OK
    Pegar o nome do produto -> OK
    Pegar o valor do produtoPegar o fabricante -> OK
    Pegar a % do desconto do produto -> OK

    Salvar o arquivos em xlsx -> OK
'''
from bs4 import BeautifulSoup
import requests

import openpyxl

def ConsultarQuantidadePagina(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='page-template') #retorna o primeiro resultado
        div = pagina.find_all('div', class_='text-center pt-3') # retorna TODOS os resultados
        div = div[-1].text
        qntd = div.split(' ')[-1]
        return qntd

def ConsultarProdutoPagina(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='list-products page-content')
        produtos = pagina.find_all('div', class_ = 'desc position-relative')

        lista_produtos = []

        for item in produtos:
            nome = item.find('h2', class_= 'title').text.strip()
            fabr = item.find('span', class_= 'font-size-11 text-primary font-weight-bold').text.strip()
            
            if bool(item.find('p', class_='sale-price')):
                prec = item.find('p', class_='sale-price').text.strip()
            else:
                prec = 'sem estoque'
            
            if bool(item.find('span', class_='discount')):
                desc = item.find('span', class_= 'discount').text.strip()
            else:
                desc= ''

#            print(fabr, ' | ', nome, ' | ', prec, ' | ', desc)

            lista_produtos.append([
                fabr,
                nome,
                prec,
                desc
            ])
        return lista_produtos
'''
def ConsultarFabricanteProduto(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='list-products page-content')
        produtos = pagina.find_all('div', class_ = 'desc position-relative')

        for item in produtos:
            nome = item.find('span', class_= 'font-size-11 text-primary font-weight-bold').text.strip()
            
            print(nome)

def ConsultarValorProduto(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='list-products page-content')
        produtos = pagina.find_all('div', class_ = 'desc position-relative')

        for item in produtos:
            nome = item.find('p', class_= 'sale-price').text.strip()
            print(nome)

def ConsultarDescontoProduto(url):
    resposta = requests.get(url)

    if resposta.status_code == 200:
        soup = BeautifulSoup(resposta.text, 'html.parser')
        pagina = soup.find('div', class_='list-products page-content')
        produtos = pagina.find_all('div', class_ = 'desc position-relative')

        for item in produtos:
            nome = item.find('span', class_= 'discount').text.strip()
            print(nome)
'''


def GravarArquivoXLSX(dados, nome_arquivo):
    try:
        excel = openpyxl.Workbook()
        planilha = excel.active

        for linha in dados:
            planilha.append(linha)

        excel.save(nome_arquivo + 'xlsx')
        print('Dados salvo com sucesso no arquivo {}.xlsx'.format(nome_arquivo))
    except Exception as ex:
        print('Error: {}'.format(ex))

area = 'hortifruti'

url = 'https://www.superpaguemenos.com.br/{}/'.format(area)
qntd = ConsultarQuantidadePagina(url)
print(qntd, 'valor de paginas')

for i in range(1, int( qntd) +1):
    new_url = url + '?p=' + str(i)
    print(new_url)
    produtos = ConsultarProdutoPagina(new_url)

GravarArquivoXLSX(produtos, area)
#ConsultarQuantidadePagina(url)
#ConsultarFabricanteProduto(url)
#ConsultarValorProduto(url)
#ConsultarDescontoProduto(url)


