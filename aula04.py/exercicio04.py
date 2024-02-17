# for i in range(30)
# print('Palmeiras maior do Brasil')

texto = "Lorem ipsum"

#pegar o numero do usuário e calcular a tabuada desse número

for i in range(10,31):
  print(i)


#pegar o numero do usuário e calcular a tabuada desse número



tabuada= int(input("Tabuada do numero: "))

for i in range(1,11):
    soma = i* tabuada
    print('{} x {} = {}' .format(tabuada, i, soma))

## dados
    
dados = (('Paulo' ,24, 1.70),
        ('Flavio' ,38, 1.71),
        ('Igor' ,21, 1.72),
        ('Victor' ,19 ,1.73),
        ('Vitoria' ,27, 1.74))

for linha in dados:
  print(linha, '<--')
  for info in linha:
    print(info, '<=')


#while

contador = 0


while contador < 10:
  print('O numero é 10')
  contador = contador + 1


  #menu while jogo

while True:
  print('1-jogar')
  print('2-opções')
  print('3-sair')

  opcao = int(input('Qual sua escolha: '))

  if (opcao == 1):
    print('Você esta jogando...')
  elif (opcao == 2):
    print('Você está configurando o jogo...')
  elif (opcao == 3):
    print('Você está saindo do jogo')
  break


#receber um numero e conferir se ele é primo:

numero = int(input('Numero: '))
contador = 1
ehPrimo = 0

while contador < numero + 1:

  if numero % contador == 0:
    ehPrimo += 1

  contador += 1

if ehPrimo == 2:
  print('O numero {} é PRIMO'.format(numero))
else:
  print('O numero {} NÃO é primo'.format(numero))


  #sequencia Fibonatica

num = int(input("Qual a posição escolhida:"))
ultimo = 1
penultimo = 0

if num == 1:
  print(penultimo)
elif num == 2:
  print(ultimo)
else:
  count = 3
  while count <= num:
    atual = ultimo + penultimo
    ultimo = atual
    penultimo = ultimo
    ultimo = atual
    count += 1
  print(atual)