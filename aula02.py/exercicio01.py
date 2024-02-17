#um script que soma 2 numeros

numero1 = input('Digite o primeiro numero:')
numero2 = input('Digite o segundo numero:')
#todas informações que são recebidas do 'input' é no formato texto (tring ou str)
#print('A soma entre {} e {} é igual a {}' .format(numero1, numero2, numero1 + numero2))
print('A soma entre {} e {} é igual a {}' .
      format(numero1, numero2, int (numero1) + int (numero2)))



#texto -> String -> str
#numeros INTEIROS -> int
#numeros DECIMAIS -> float

#tipostring = input('Digite um texto: ')
#print(type(tipostring))

valorInput = input('Digite um numero inteiro')
print(type(valorInput), 'tipo da variavel "valorInput"')
tipoInteiro = int(valorInput)
print(type(tipoInteiro), 'tipo da variavel "tipoInteiro"')
tipoFloat = float(valorInput)
print(type(tipoFloat), 'tipo da variavel "tipoFloat" ')



valor = input('Digite um numero: ')

print('valor é numerico: ', valor.isnumeric()) #verifica se o numero é inteiro

print('valor é numerico: ', valor.isdecimal()) #verifica se o numero é decimal
print(type(valor), valor)


texto = input('digite um texto: ')

print('1. Quantidade de caracter: ', len(texto))
print('2. Nome em MAIUSCULO: ', texto.upper())
print('3. Nome em minusculo: ', texto.lower())
print('4. None em minusculo: ', texto.capitalize())
espaco = texto.find(' ')
print('5. Procura de informações', texto[espaco:])
print('6. Troca de Valores', texto.replace('o','a'))
print('7. Verificar se tem somente LETRAS', texto.isalpha())
print('8. Verificar se tem letras ou numeros', texto.isalnum())
# print('9. Quebrar o texto', texto.split[1])
# texto.Split = texto.Split(' ')
# print('9. quabrar texto', textoSplit[0] )
print('10. Centralizar o texto')
print(texto.center(100,'*'))


#Operadores

num1 = input('digite o primeiro numero: ')
num2 = input('digite o segundo numero: ')

soma = int(num1) + int(num2)
print('Valor da soma {} '.format(soma))

subtracao = int(num1) - int(num2)
print('Valor subtracao {}' .format(subtracao))

multipicacao = int(num1) * int(num2)
print('Valor multiplicacao {}' .format(multipicacao))

divisao = int(num1) / int(num2)
print('Valor divisao {:.2f}' .format(divisao))


#if

altura = input('Qual sua altura em centimetros: ')
#print(type(altura))
if int(altura) > 160:
  print('voce pode ir na montanha russa!')

else:
  print('voce não pode ir na montanha russa!')
