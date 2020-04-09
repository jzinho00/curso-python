d = int(input('Por quantos dias o Carro foi alugado? '))
km = float(input('Quantos Km o carro andou? '))
p = (d * 60)+(km * 0.15)
print('O total a pagar é R${:.2f}'.format(p))
