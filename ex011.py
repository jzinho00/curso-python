l = float(input('Qual a largura da parede? '))
al = float(input('Qual a altura da parede? '))
ar = l * al
print('Área: {}m²'.format(ar))
print('Quantidade de tinta necessária: {:.1f}L'.format(ar / 2))
