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

#Menu jogo pedra papel tesoura

  import random
 
continuar = 's'
jogada = ('Pedra', 'Papel', 'Tesoura')
resultado = ((0,-1,1),(1,0,-1),(-1,1,0))
placarJogador = 0
placarComputador = 0
 
while continuar.lower() == 's':
  escolha = int(input('''Escolha uma opção para se jogar:
  [1] Pedra
  [2] Papel
  [3] Tesoura
Digite sua escolha: '''))
 
  computador = random.randint(0, 2)
 
  print('jogador: ', jogada[escolha-1])
  print('computador: ', jogada[computador])
 
  res = resultado[escolha-1][computador]
 
  if res == -1:
    print("você perdeu!")
    placarComputador += 1
  elif res == 0:
    print("empate!")
  elif res == 1:
    print("\033[1;34mvocê venceu!!! \033[0m")
    placarJogador += 1
 
  continuar = input('aperte \'S\' para continuar: ')
 
print('jogador {} x {} computador'.format(placarJogador, placarComputador))