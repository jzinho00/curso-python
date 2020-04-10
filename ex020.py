from random import shuffle
n1 = input('Digite o primeiro aluno: ')
n2 = input('Digite o segundo aluno: ')
n3 = input('Digite o terceiro aluno: ')
n4 = input('Digite o quarto aluno: ')
list = [n1, n2, n3, n4]
shuffle(list)
print('A ordem será: \n{}'.format(list))