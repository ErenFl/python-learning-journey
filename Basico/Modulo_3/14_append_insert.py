#Agregando elementos a una lista: append() y insert()

'''El metodo append(), toma el valor de su argumento y lo coloca al final de la lista '''
numbers = [111, 7, 2, 1]
print("Longitud original: ", len(numbers))
print("Lista original: ",numbers)

#list.append(value) /// append solo agrega UN ELEMENTO cada vez
numbers.append(4) #Inserta el 4 al final de la lista

print("Longitud nueva: ",len(numbers))
print("Lista nueva: ",numbers)

'''El método insert() puede agregar un nuevo elemento en cualquier lugar de la lista, 
no solo al final.'''
#list.insert(location, value)
numbers.insert(0, 222) #Indice = 0, Numero = 222
numbers.insert(1, 333)
print(len(numbers))
print("Lista actualizada: ", numbers)


#Ejercicio 2: Lista vacia
my_list = []  # Creando una lista vacía.

for i in range(5):
    my_list.append(i + 1)

print(my_list)


#Ejercicio 3: Almacena datos en orden inverso
my_list = []  # Creando una lista vacía.
 
for i in range(5):
    my_list.insert(0, i + 1)
 
print(my_list)



