
#Se debe imprimir el valor mas grande

#EJERCICIO 1
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)
 
#--------------------------------------------------------
 
#EJERCICIO 2
# Se leen dos números
number1 = int(input("Ingresa el primer número: "))
number2 = int(input("Ingresa el segundo número: "))
 
# Elige el número más grande
if number1 > number2: larger_number = number1
else: larger_number = number2
 
# Imprime el resultado
print("El número más grande es:", larger_number)
 
#--------------------------------------------------------

#Ejercicio 3 (CON TRES NUMEROS )
 
num1 = int(input("Ingresa un numero: "))
num2 = int(input("Ingresa un numero: "))
num3 = int(input("Ingresa un numero: "))

if num2 < num1 > num3:
    Num_Mayor = num1
elif num1 < num2 > num3:
    Num_Mayor = num2
else: 
    Num_Mayor = num3
    
print(Num_Mayor)

#--------------------------------------------------------

#Ejercicio 4 FORMA FACIL:

numero1 = int(input("Ingresa un numero: "))
numero2 = int(input("Ingresa un numero: "))
numero3 = int(input("Ingresa un numero: "))

Num_Mayor = max(numero1,numero2, numero3) # Verifica cuál de los números es el mayor
Num_Menor = min(numero1,numero2, numero3) # Verifica cuál de los números es el menor
print(Num_Mayor)
print(Num_Menor)