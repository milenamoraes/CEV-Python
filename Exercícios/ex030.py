'''Crie um programa que leia um número inteiro e mostre na tela se ele é PAR ou IMPAR.  '''
numero = int(input('Me diga um número qualquer:'))
resultado = numero % 2
cores = {
    'limpa' : '\033[m',
    'azul' : '\033[4;34m',
    'lilas' : '\033[4;35m'}
if resultado == 0:
    print('O número {}{}{} é PAR'.format(cores['azul'], numero, cores ['limpa']))
else:
    print('O número {}{}{} é ÍMPAR'.format(cores['lilas'],numero, cores['limpa']))