'''Escreva um programa que leia a velocidade de um carro.
Se ele ultrapassar 80km/h, mostre uma mensagem dizendo que ele foi multado.
a multa vai custar R$7,00 por cada km acima do limite.'''
velocidade = float(input('Qual é a velocidade atual do carro?'))
if velocidade > 80:
    print('\033[4;31mMULTADO! Você excedeu o limite permitido que é de 80Km/h')
    multa = (velocidade - 80) * 7
    print('Você deve pagar uma multa de R${:.2f}!\033[m'.format(multa))
print('\033[34mTenha um bom dia! Dirija com segurança')