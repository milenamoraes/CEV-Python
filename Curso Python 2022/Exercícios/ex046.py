'''FAÇA UM PROGRAMA QUE MOSTRE NA TELA UMA CONTAGEM REGRESSIVA PARA O ESTOURO DE FOGOS DE ARTIFICIO,
INDO DE 10 ATÉ 0, COM UMA PAUSA DE 1 SEGUNDO ENTRE ELES.'''
'''from time import sleep
import emoji
print('10')
sleep(1)
print('09')
sleep(1)
print('08')
sleep(1)
print('07')
sleep(1)
print('06')
sleep(1)
print('05')
sleep(1)
print('04')
sleep(1)
print('03')
sleep(1)
print('02')
sleep(1)
print('01')
sleep(1)

print(emoji.emojize('BUM! BUM! POOOOW :tada:', use_aliases=True))'''

import emoji
from time import sleep
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print(emoji.emojize('BUM! BUM! POOOOW :tada:', use_aliases=True))


