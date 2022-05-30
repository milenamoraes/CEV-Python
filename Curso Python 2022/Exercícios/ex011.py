#FAÇA UM PROGRAMA QUE LEIA A LARGURA E A ALTURA DE UMA PAREDE EM METROS, CALCULE A SUA AREA
#E A QUANTIDADE DE TINTA NECESSARIA PARA PINTÁ-LA, SABENDO QUE CADA LITRO DE TINTA PINTA UMA AREA DE 2M².
larg = float(input('Largura da parade:'))
alt = float(input('Altura da parade:'))
area = larg * alt
print('Sua parade tem a dimensão de {}x{} e sua área é de {}m².'.format(larg, alt, area))
tinta = area / 2
print('Para pintar essa parede, você precisará de {}l de tinta'.format(tinta))
