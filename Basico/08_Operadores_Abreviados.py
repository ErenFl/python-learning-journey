#Expresiones               Operador Abreviado
'''
i = i + 2 *j    -------------> i += 2 * j

var = var / 2   -------------> var /= 2

rem = rem % 10  -------------> rem %= 10

j = j - (i + var + rem)  ----> j -= (i + var + rem)

x = x ** 2      -------------> x **= 2

x = x * 2       ------------->  x *= 2

sheep = sheep + 1  ---------> sheep += 1

'''
#EJERCICIO 1
'''
Teniendo en mente que 1 milla equivale aproximadamente a 1.61 kilómetros, 
complementa el programa para que convierta de:
Millas a kilómetros;
Kilómetros a millas.


SALIDA ESPERADA
7.38 millas son 11.88 kilómetros
12.25 kilómetros son 7.61 millas

'''


kilometers = 12.25
miles = 7.38

miles_to_kilometers = miles * 1.61
kilometers_to_miles = kilometers / 1.61

print(miles, "millas son", round(miles_to_kilometers, 2), "kilómetros")
print(kilometers, "kilómetros son", round(kilometers_to_miles, 2), "millas")




#EJERCICIO 
'''
Observa el código en el editor: lee un valor float, lo coloca en una variable llamada x, 
e imprime el valor de la variable llamada y. Tu tarea es completar el código para evaluar 
la siguiente expresión:

3x^3 - 2x2 + 3x - 1
El resultado debe ser asignado a y.
'''
print()

x =  0
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x -1)
print("y =", y)


x =  1
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x -1)
print("y =", y)


x =  -1
x = float(x)
y = (3*x**3 - 2*x**2 + 3*x -1)
print("y =", y)

#############
a = 6
b = 3
a /= 2 * b
print(a)

