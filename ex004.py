x = input('digite algo: ')

print ('Esta é uma variavel do tipo: {} '.format(type(x)))
print('É do tipo numérico?', x.isnumeric())
print ('É uma letra?', x.isalpha())
print ('É alphanumérico?', x.isalnum())
print ('Esta em maiúsculo? ', x.isupper())
print ('Esta em minúsculo? ', x.islower())
print ('Esta capitalizada? ',x.istitle())

