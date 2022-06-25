'''Escreva um programa que faça o computador "pensar" em um número inteiro entre 0 e 5 e peça para o usuário tentar
descobrir qual foi o número escolhido pelo computador. O programa deverá escrever na tela se o usuário venceu ou não.'''
from random import randint
from time import sleep
computador = randint(0,5) # Faz o computador "pensar"
cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[1;31m',
    'amarelho' : '\033[1;33m',
    'azul' : '\033[4;34m' }
n = 0
n1 = 5
print('-=-' * 20)
print('Vou pensar em um número entre {}{}{} e {}{}{}. Tente adivinhar...'.format(cores ['azul'], n, cores ['limpa'], cores ['vermelho'], n1, cores['limpa']))
print('-=-' * 20)
jogador = int(input('Em que número eu pensei?')) # Jogador tentar adivinhar
print('\033[4;33mPROCESSANDO...\033[m')
sleep(2)
if jogador == computador:
    print('\033[4;32;40mPARABÉNS! Você conseguiu me vencer!\033m')
else:
    print('\033[4;31;40mGANHEI! Eu pensei no número {} e não no {}!\033[m'.format(computador, jogador))
