p = float(input('Qual o preço do produto? R$'))
c = p / 100 * 5

print('Com o desconto de 5%, o novo preço é R${:.2f}'.format(p - c))

