

x = int(input()) #11
y = int(input()) #4

x = x % y #  11 % 4 = 2,   x = 3

'''Cuando el número de la izquierda es menor que el de la derecha,
el residuo es el mismo número. '''
x = x % y #  3 % 4 = 3,   x = 3
y = y % x #  4 % 3 = 2,   x = 1

print(y)


