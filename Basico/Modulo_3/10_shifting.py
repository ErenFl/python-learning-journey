#Esto se aplica solo a los valores de número entero, y no debe usar flotantes como argumentos para ello.
'''  Los operadores de cambio en Python son un par de dígrafos: < < y > >
sugiriendo claramente en qué dirección actuará el cambio.'''

var = 17
var_right = var >> 1 #  --->  17//2 (17 dividido entre 2 a la potencia de 1) → 8 
        #Desplazarse hacia la derecha en un bit equivale a la división entera entre dos

var_left = var << 2 # ---> 17 * 4 (17 multiplicado por 2 a la potencia de 2) → 68 
#Desplazarse hacia la izquierda dos bits es lo mismo que multiplicar números enteros por cuatro

print(var, var_left, var_right)


#Ejercicio 1

x = 4
y = 1
 
a = x & y
b = x | y
c = ~x  # ¡difícil! 4 = 0100 y ~4 es 1011 = 5
d = x ^ 5 #XOR
e = x >> 2
f = x << 2
 
print(a, b, c, d, e, f)
