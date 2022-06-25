'''FAÇA UM PROGRAMA QUE CALCULE A SOMA ENTRE TODOS OD NÚMEROS IMPARES QUE SÃO MÚLTIPLOS DE TRÊS E QUE
SE ENCONTRAM NO INTERVALO DE 1 ATÉ 500.'''
soma = 0
cont = 0
for c in range(1, 501, 2):
    if c % 3 == 0:
        soma = soma + c
        cont = cont + 1
print('A soma de todo os {} valores solicitados é {}'.format(cont, soma))