'''  Los elementos dentro de una lista pueden tener diferentes tipos. 
Algunos de ellos pueden ser enteros, otros son flotantes y otros pueden ser listas'''

numbers = [10, 5, 7, 2, 1]

print("Contenido de la lista:", numbers)  # Imprimiendo contenido de la lista original.

print(numbers[0]) # Accediendo al primer elemento de la lista.

numbers[0] = 111 #Cambiar el valor al primer elemento
print("Nuevo contenido de la lista: ", numbers)  # Contenido actual de la lista.

numbers[1] = numbers[4]  # Copiando el valor del quinto elemento al segundo elemento.
print("Nuevo contenido de la lista:", numbers)  # Imprimiendo el contenido de la lista actual.

print("\nLongitud de la lista:", len(numbers))  # Imprimiendo la longitud de la lista.
#length - longitud

''' El valor dentro de los corchetes que selecciona un elemento de la lista se llama
un índice, mientras que la operación de seleccionar un elemento de la lista se conoce 
como indexación.'''