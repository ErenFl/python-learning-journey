            #Break and Continue
            
'''
break - sale del bucle inmediatamente, e incondicionalmente termina la operación del bucle;
el programa comienza a ejecutar la instrucción más cercana después del cuerpo del bucle.

continue - se comporta como si el programa hubiera llegado repentinamente al final del 
cuerpo; el siguiente turno se inicia y la expresión de condición se prueba de inmediato
'''
'''
# break - ejemplo
print("La instrucción break:")
for i in range(1, 6):
    if i == 3:
        break #Rompe el bucle justo en ese momento
    print("Dentro del bucle.", i)
print("Fuera del bucle.")


# continue - ejemplo
print("\nLa instrucción continue:")
for i in range(1, 6):
    if i == 3:
        continue #Aun que la condicion se cumple, obliga a continuar sin la interrupcion
    print("Dentro del bucle.", i)
print("Fuera del bucle.")

'''


largest_number = -99999999
counter = 0

while True:
    number = int(input("Ingresa un número o escribe -1 para finalizar el programa: "))
    if number == -1:
        break
    counter += 1
    if number > largest_number:
        largest_number = number

if counter != 0:
    print("El número más grande es", largest_number)
else:
    print("No has ingresado ningún número.")
