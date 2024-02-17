import random
from os import system
def escolher_palavra():
    palavras = ['python', 'java', 'ruby', 'javascript', 'html', 'css', 'php']
    return random.choice(palavras)

def mostrar_palavra(palavra ,letra_escolhidas):
    exibicao = ''
    for letra in palavra:
        if letra in letra_escolhidas:
            exibicao += letra
        else:
            exibicao += '_'
    return exibicao


def jogar():
    system('cls')
    palavra_secreta = escolher_palavra()
    tentativas_restante = 7
    letras_escolhidas = []

    print('''
   __     ______     ______     ______        ______   ______     ______     ______     ______    
  /\ \   /\  __ \   /\  ___\   /\  __ \      /\  ___\ /\  __ \   /\  == \   /\  ___\   /\  __ \   
 _\_\ \  \ \ \/\ \  \ \ \__ \  \ \ \/\ \     \ \  __\ \ \ \/\ \  \ \  __<   \ \ \____  \ \  __ \  
/\_____\  \ \_____\  \ \_____\  \ \_____\     \ \_\    \ \_____\  \ \_\ \_\  \ \_____\  \ \_\ \_\ 
\/_____/   \/_____/   \/_____/   \/_____/      \/_/     \/_____/   \/_/ /_/   \/_____/   \/_/\/_/
''')
    print('Bem vindo(a) ao jogo da forca da galerinha do Python')
    print('Adivinhe a palavra secreta: Tema Linguagem de programação')
    print(mostrar_palavra(palavra_secreta, letras_escolhidas))

    while tentativas_restante > 0:
        letra = input('Digite uma letra: ').lower()
        
        if len(letra) != 1 or letra.isnumeric():
            print('Por favor digite apenas uma letra.')
            continue
        
        if letra in letras_escolhidas:
            print('Você já usou essa letra, tente outra.')
            continue

        
        letras_escolhidas.append(letra)

        if letra not in palavra_secreta:
            tentativas_restante = tentativas_restante - 1 # tentativas_restante -= 1
            print('letra incorreta 😒. Você tem {} tentativas restantes.'.format(tentativas_restante))
        else:
            print('Letra correta 👍!')

        palavra_mostrar = mostrar_palavra(palavra_secreta, letras_escolhidas)
        print(palavra_mostrar)

        if palavra_mostrar == palavra_secreta:
            print('Voce acertou!!!')
            break
    if(tentativas_restante == 0):
        print('Voce Perdeu!!! ')
            
# 1 - verificar se a letra foi acertada
# 2 - criar um laço para o usuario continuar a jogar
op = ''
while op.lower() != 's':       
    jogar()
    op = input('Digite "S" para sair: ')
