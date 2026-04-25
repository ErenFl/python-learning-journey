#Ejercicio 1
'''Crea un bucle for que cuente de 0 a 10, e imprima números impares en la pantalla'''
for i in range(0,11):
	if i%2 == 1 
	print ("Numero impar: ", i)

#Ejercicio 2
'''Crea un bucle while que cuente de 0 a 10, e imprima números impares en la pantalla'''
x=0
while x < 11:
    if x%2 != 0:
        print(x)
    x += 1

#Ejercicio 3
'''Crea un programa con un bucle for y una sentencia break que itere sobre los caracteres
en una dirección de correo, salir cuando el bucle encuentre el carácter @ e imprimir todo
lo anterior en una linea'''

for ch in "john.smith@pythoninstitutee.org":
    if ch != "@":
        print(ch, end="") #Evita el salto de linea
    else:
        break

#Ejercicio 4
''' Crea un programa con un bucle for y una sentencia continue. El programa debe iterar 
sobre ua cadena de dígitos y remplazar cada 0 con x e imprimir la cadena modificada'''

for digit in "0165031806510":
    if digit != "0":
        print(digit, end="")
        continue
    else:
        digit = "x"
        print(digit, end="")

#Ejemplo 5

for i in range(0,6,3)
	print(i)
