import math
a = float(input('Digite o angulo desejado: '))
seno = math.sin(math.radians(a))
cos = math.cos(math.radians(a))
tan = math.tan(math.radians(a))
print('O seno de {} é {:.2f}'.format(a, seno))
print('O cosseno de {} é {:.2f}'.format(a, cos))
print('A tangente de {} é {:.2f}'.format(a, tan))