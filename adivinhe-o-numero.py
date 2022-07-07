from random import randint
from time import sleep
computador = randint(0,10)
c = 1
print('-=-' * 19)
print(' Vou pensar em um número entre 0 e 10. Tente adivinhar...')
print('-=-' * 19)
jogador = int(input('Em que número eu pensei? '))
print('PROCESSANDO...')
sleep(2)
while jogador != computador:
    if jogador < computador:
        print('Mais... Tente mais uma vez.')
    elif jogador > computador:
        print('Menos... Tente mais uma vez.')
    jogador = int(input('Qual seu palpite? '))
    c = c + 1
print(f'Acertou com {c} tentativa(s). Parabéns!')