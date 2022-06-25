'''Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o ultimo nome separadamente.
ex: Milena de Paula Moraes
primeiro = Milena
ultimo = Moraes'''
n = str(input('Digite seu nome completo:')).strip()
nome = n.strip()
print('Muito prazer em te conhecer!')
print('Seu primeiro nome é {}'.format(nome[0]))
print('Seu último nome é {}'.format(nome[len(nome)-1]))

