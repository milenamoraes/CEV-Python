'''Faça um programa que leia três números e mostre qual é o maior e qual é o menor.'''
a = int(input('Primeiro valor:'))
b = int(input('Segundo valor:'))
c = int(input('Terceiro valor:'))
cores = {
    'limpa' : '\033[m',
    'vermelho' : '\033[7;31m',
    'amarelho' : '\033[7;33m'
}
# Verificando quem é menor
menor = a
if b<a and b<c:
    menor = b
if c<a and c<b:
    menor = c
# Verificando quem é o maior
maior = a
if b>a and b>c:
    maior = b
if c>a and c>b:
    maior = c
print('O menor valor digitado foi {}{}{}'.format(cores['vermelho'], menor, cores['limpa']))
print('O maior valor digitado foi {}{}{}'.format(cores['amarelho'], maior, cores['limpa']))