#for c in range (...
'''for c in range(0, 4):
     n = int(input('Digite um valor: '))
print('fim')'''

i = int(input('Início: '))
f = int(input('Fim: '))
p = int(input('Passo: '))
for c in range(i, f+1, p):
    print(c)
print('FIM')