#Exercicio_Python

#Calcule a média das 4 notas de um aluno

nota1 = input('Digite a primeira nota:')
nota2 = input('Digite a segunda nota:')
nota3 = input('Digite a terceira:')
nota4 = input('Digite a quarta nota:')

media = float(nota1) + float(nota2) + float(nota3) + float(nota4)
soma_media = media/4
print(soma_media)

if float(soma_media) >= 8:
  print('Voce foi aprovado')
elif float(soma_media) >= 5:
  print('ainda há esperança')
else:
  print('fica pro ano que vem')

## outro exercicio
numero1 = 5
numero2 = 3

potencia = numero1 ** numero2
modulo = numero1 % numero2

print(potencia)

#par_impar

numero = input('Digite um numero: ')
soma = int(numero) %2

if (soma) == 0:
  print ('O numero é par: ')

else:
  print('o numero  é impar ')


#imc

peso = input('Digite seu peso: ')
altura = input('Digite sua altura: ')

imc = float(peso) / (float(altura) * float(altura))
print(imc)

if imc >= 40:
  print('Obeso Morbido')

elif imc >= 30:
  print('Obeso')

elif imc >= 25:
  print('Sobrepeso')

elif imc >= 18:
  print('Peso saudavel')

elif imc < 18.5:
  print('abaixo do peso')

