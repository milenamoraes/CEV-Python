#exemplo 1
'''print('\033[0;31mOlá, Mundo!\033[m')'''

#exemplo 2
'''a = 4
b = 8
print('\033[31m{}\033[m ou \033[33m{}\033[m '.format(a, b))'''

#exemplo 3
'''nome = 'Milena de Paula'
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'. format('\033[4;33;40m', nome, '\033[m'))'''

#exemplo 4
nome = 'Milena'
cores = {'limpa' : '\033[m',
         'vermelho' : '\033[4;31m',
         'azul' : '\033[1;34m',
         'amarelo' : '\033[4;33m',
         'verde' : '\033[7;32m'}
print('Olá! Muito prazer em te conhecer, {}{}{}!!!'.format(cores['vermelho'], nome, cores['limpa']))