'''Desenvolva um programa que pergunte a distânia de uma viagem em km. Calcule o preço da passagem, cobrando
R$0,50 por km para viagens de até 200km e R$0,45 para viagens mais longas.'''

distancia = float(input('Qual é a distância da sua viagem?'))
cores = {
    'limpa' : '\033[m',
    'verde' : '\033[4;32m',
    'amarelo' : '\033[4;33m'
}
print('Você está prestes a começa uma viagem de {}{}km'.format(cores['verde'], distancia))
# preco = distancia * 0.50 if distancia <= 200 else distancia * 0.45
if distancia <= 200:
    preco = distancia * 0.50
else:
    preco = distancia * 0.45
print('\033[mE o preço da sua passagem será de {}R${:.2f}{} '.format(cores['amarelo'], preco, cores['limpa']))
