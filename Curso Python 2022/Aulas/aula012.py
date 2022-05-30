# CONDIÇÕES ALINHADAS

nome = str(input('Qual é o seu nome?')).strip()
if nome == 'Milena':
     print('Que nome bonito')
elif nome == 'Frida' or nome == 'Granola' or nome == 'Manuela' or nome == 'Karina':
     print('Seu nome é bem popular no Brasil!')
elif nome in 'Maria Julia Bruna':
     print('Que belo nome feminino')
else:
     print('Seu nome é bem normal.')
print('Tenha um bom dia, {}!'.format(nome))