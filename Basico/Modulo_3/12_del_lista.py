''' Cualquier elemento de la lista puede ser eliminado en cualquier momento
esto se hace con una "instrucción" llamada "del" (eliminar).'''
numbers = [10, 5, 7, 2, 1]

del numbers[1]
print("Longitud de la nueva lista:",len(numbers))
print("\nNuevo contenido de la lista:",numbers)

#No puedes acceder a un elemento que no existe - no puedes obtener su valor ni asignarle un valor
print(numbers[4]) #Error, no existe el indice 4 despues de borrar el indice 1
numbers[4] = 1