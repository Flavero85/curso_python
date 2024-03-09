print("Hello Word. ", "Esse é meu primeiro programa", "em Python")

print("Olá meu nome é {} e tenho {} anos". format("Rafael", "38"))

input('Quantos anos você tem? ')

print('Eu estudo no {}'.format(input('Onde você estuda? ')))

print('Eu moro na rua {}, {}, {}, Nova Odessa-SP ' .
format(input("rua: "), input("numero: "), input("bairro: "), input("cidade:")))
## rua: yolanda
## numero: 32
## bairro: europa
## cidade:nova odessa
## Eu moro na rua yolanda, 32, europa, Nova Odessa-SP

nome = input('Qual o seu nome? ')
sobrenome = input('Qual o seu sobrenome? ')
idade = input('Qual a sua idade? ')
## print('Olá me chamo {}, e tenho {} anos ' .format(nome, sobrenome, idade))
## Qual o seu nome? flavio
## Qual o seu sobrenome? rafael
## Qual a sua idade? 38
## Olá me chamo flavio, e tenho rafael anos

rua = input('Qual o nome da sua rua? ')
numero = input('Qual o seu numero? ')
bairro = input('Qual o seu bairro? ')
cidade = input('E a sua cidade? ')
print('Eu moro na rua {}, numero {}, no bairro {}, e na cidade de {}' .format(rua, numero, bairro, cidade))
## Qual o nome da sua rua? yolanda
## Qual o seu numero? 32
## Qual o seu bairro? jardim europa
## E a sua cidade? nova odessa
## Eu moro na rua yolanda, numero 32, no bairro jardim europa, e na cidade de nova odessa