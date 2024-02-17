#Tupla é criado com () e não pode seus dados alterados
#Array é criado com [] e pode ter seus dados alterados

numeros = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove')
dez = ('dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove')
dezenas = ('', '', 'vinte', 'trinta', 'quarenta', 'cinquenta', 'sessenta', 'setenta', 'oitenta', 'noventa')

posicao = int(input("Digite um numero entre 0 e 99: "))
if posicao < 10:
  print(numeros[posicao])
elif posicao < 20:
  print(dez[posicao - 10])
elif posicao <= 99:
  
  dezena = int(posicao / 10) #int(str(posicao)[0:1])
  numeral = int(posicao % 10) #int(str(posicao)[1:2])

  if numeral != 0:
    print('{} e {}' .format(dezenas[dezena], numeros[numeral]))
  else:
    print('{}'.format(dezenas[dezena], numeros[numeral]))