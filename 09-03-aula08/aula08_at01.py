from bs4 import BeautifulSoup
import requests

url = 'https://www.paulowh.com'

resposta = requests.get(url)

if resposta.status_code == 200:
    soup = BeautifulSoup(resposta.text, 'html.parser')

    section = soup.find('section', id='experience')

    for row in section.find_all('div',class_='card-content'):
        cargo = row.find('h6' , class_='timeline-title')
        print(cargo.text)

    for row in section.find_all('div',class_='card-content'):
        empresa = row.find('h6' , class_='empresa')
        print(empresa.text.strip())

    for row in section.find_all('div',class_='card-content'):
        periodo = row.find('h6' , class_='periodo')
        print(periodo.text.strip())

    for row in section.find_all('div',class_='card-content'):
        paragrafo = row.find('p')
        print(paragrafo.text.strip())
