from bs4 import BeautifulSoup
import requests

# # def consultaSitePagueMenos(url):
# #     respostas = requests.get(url)

# #     if respostas.status_code == 200:
# #         soup = BeautifulSoup(respostas.text, 'html.parser')
# #         page = soup.find('div', class_='list-products page-content')

# #         prod_paguemenos = []
# #         for row in page.find_all('div', class_='desc position-relative'):
# #             produto = row.find('h2').text.strip()
# #             preco = row.find('p', class_='sale-price').text.strip()
# #             prod_paguemenos.append([
# #                 produto,
# #                 preco
# #             ])

# #             return prod_paguemenos


# url = 'https://www.superpaguemenos.com.br/hortifruti/'
# consultaSitePagueMenos(url)

def consultaSiteSaoVicente(url):
    respostas = requests.get(url)

    if respostas.status_code == 200:
        soup = BeautifulSoup(respostas.text, 'html.parser')
        page = soup.find('div', class_='searchResults__wrapper')

        print(page)

        # prod_saovicente = []
        # for row in page.find_all('div', class_='productCard__container'):
        #     produto = row.find('span', class_='productCard__body').text.strip()
        #     preco = row.find('span', class_='productList__item__price').text.strip()



url = 'https://www.svicente.com.br/Hortifruti-3/'
consultaSiteSaoVicente(url)