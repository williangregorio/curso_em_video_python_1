n = input('Digite algo: ')
print(type(n))
print('É numérico? {}'.format(n.isnumeric()))
print('E Alfanumérico? {}'.format(n.isalnum()))
print('E Alfa? {}'.format(n.isalpha()))
print('E Decimal? {}'.format(n.isdecimal()))

