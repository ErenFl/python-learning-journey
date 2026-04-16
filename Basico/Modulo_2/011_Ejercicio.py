'''
Escenario
Tu tarea es completar el código para evaluar los resultados de cuatro operaciones 
aritméticas básicas.

Los resultados deben imprimirse en la consola.
'''
# ingresa un valor flotante para la variable a aquí
# ingresa un valor flotante para la variable b aquí

# mostrar el resultado de la suma aquí
# mostrar el resultado de la resta aquí
# mostrar el resultado de la multiplicación aquí
# mostrar el resultado de la división aquí

var_a = float(input("Asigna un valor a \"A\" "))
var_b = float(input("Asigna un valor a \"B\" \n"))

suma = var_a + var_b
rest = var_a - var_b
mult = var_a * var_b
divi = var_a / var_b

print(var_a,"+", var_b,"=",suma)
print(var_a,"-", var_b,"=",rest)
print(var_a,"*", var_b,"=",mult)
print(var_a,"/", var_b,"=",divi)

print("\n¡Eso es todo, amigos!")