# . -> pasta atual
# .. -> retorno de pasta

caminho_arquivo = 'categorias.csv'

# r -> read -> leitura
# w -> write -> escrita
categorias = open(caminho_arquivo, 'r', encoding='utf-8')

lista_categorias = []

##print(categorias)

for linha in categorias:
    colunas = linha.strip().split(';')
    print(colunas)