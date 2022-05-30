'''Crie um programa que faça o computador Jokenpô com você.'''
from random import randint
from time import sleep
import emoji
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)
print('''\033[1:35mSuas opções:
[ 0 ] PEDRA
[ 1 ] PAPEL
[ 2 ] TESOURA\033[m''')
jogador = int(input('\033[7:34mQual é a sua jogada?\033[m '))
print(emoji.emojize(":fist:", use_aliases=True))
print('\33[1:36mJO\033[m')
sleep(1)
print('\033[1:36mKEN\033[m')
sleep(1)
print('\033[1:36mPO!!!\033[m')
sleep(1)
print('-=' * 11)
print('\033[1:35mComputador jogou: {}'.format(itens[computador]))
print('Jogador jogou: {}\033[m'.format(itens[jogador]))
print('-=' * 11)
if computador == 0: # computador jogou PEDRA
    if jogador == 0:
        print(emoji.emojize('\033[1:33mEMPATE!\033[m :sunglasses:', use_aliases=True))
    elif jogador == 1:
         print(emoji.emojize("\033[1:32mVOCÊ VENCEU!!!\033[m:tada:", use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[1:34mCOMPUTADOR VENCEU!\033[m:smile:', use_aliases=True))
    else:
        print('\033[1:31mJOGADA INVÁLIDA!\033[m')

elif computador == 1: # computador jogou PAPEL
    if jogador == 0:
        print(emoji.emojize('\033[1:34mCOMPUTADOR VENCEU!\033[m:smile:', use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[1:33mEMPATE!\033[m :sunglasses:', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize("\033[1:32mVOCÊ VENCEU!!!\033[m:tada:", use_aliases=True))
    else:
        print('\033[1:31mOPÇÃO INVÁLIDA!\033[m')

elif computador == 2: # computador jogou TESOURA
    if jogador == 0:
        print(emoji.emojize("\033[1:32mVOCÊ VENCEU!!!\033[m:tada:", use_aliases=True))
    elif jogador == 1:
        print(emoji.emojize('\033[1:34mCOMPUTADOR VENCEU!\033[m:smile:', use_aliases=True))
    elif jogador == 2:
        print(emoji.emojize('\033[1:33mEMPATE!\033[m :sunglasses:', use_aliases=True))
    else:
        print('\033[1:31mOPÇÃO INVÁLIDA!\033[m')




















