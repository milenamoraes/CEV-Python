#FAÇA UM ALGORITMO QUE LEIA O SALÁRIO DE UM FUNCIONARIO E MOSTRE SEU NOVO SALÁRIO, COM 15% DE AUMENTO
a = float(input('Qual é o salário do funcionário? R$'))
novo = a + ( a * 15 / 100)
print('Um funcionário que ganhava R${:.2f},com de 15% aumento, passa a receber R${:.2f}'.format(a, novo))