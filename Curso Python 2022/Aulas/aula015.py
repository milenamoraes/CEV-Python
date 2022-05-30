'''cont = 1
while cont <= 10:
    print(cont, '->', end= '')
    cont += 1
print('Acabou')'''

#PRA SEMPRE 

'''cont = 1
while True: 
    print(cont, '->', end= '')
    cont += 1
print('Acabou')'''

#INTERROMPENDO REPETIÇÕES WHILE

n = s = 0
while True:
    n = int(input('Digite um número: '))
    if n == 999:
        break
    s += n
'''print('A soma vale {}'.format(s))''' #JEITO ANTIGO
print(f'A soma vale {s}') #JEITO ATUAL 