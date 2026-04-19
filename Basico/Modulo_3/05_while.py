'''
Diferencia y similitud entre If y while

La diferencia semántica es más importante: cuando se cumple la condición, if realiza sus 
sentencias sólo una vez; while repite la ejecución siempre que la condición se evalúe 
como True.
-Si la condición es False (igual a cero) tan pronto como se compruebe por primera vez, 
el cuerpo no se ejecuta ni una sola vez.
-El cuerpo debe poder cambiar el valor de la condición, porque si la condición es True al 
principio, el cuerpo podría funcionar continuamente hasta el infinito.
'''

#Bucle infinito
#while True:
#    print("Estoy atrapado dentro de un bucle.")

# Almacena el actual número más grande aquí.
largest_number = -999999999

# Ingresa el primer valor.
number = int(input("Introduce un número o escribe -1 para detener: "))

# Si el número no es igual a -1, continuaremos
while number != -1:
    # ¿Es el número más grande que el valor de largest_number?
    if number > largest_number:
        # Sí si, se actualiza largest_number.
        largest_number = number
    # Ingresa el siguiente número.
    number = int(input("Introduce un número o escribe -1 para detener: "))

# Pero si el número es igual a -1
# Imprime el número más grande.
print("El número más grande es:", largest_number)

