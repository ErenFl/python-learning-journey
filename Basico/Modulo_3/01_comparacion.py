'''
                                        IGUALDAD
 ¿son dos valores iguales?
Para hacer esta pregunta, se utiliza el == (igual igual) operador.

'''
print(2 == 2) #True

# Python puede convertir el valor entero en su equivalente real,por lo tanto es True
print(2 == 2.) #True

print(2 == 3) #False

#Ejercicio
var = 0 
print(var == 0) #True

var = 1
print(var == 0) #False

'''
                                        DESIGUALDAD
El operador != (no es igual a) también compara los valores de dos operandos.
Si son iguales, el resultado de la comparación es False. 
Si no son iguales, el resultado de la comparación es True.
'''
var = 0  
print(var != 0) #False

var = 1
print(var != 0) #True

'''
                                        MAYOR O IGUAL QUE
Su prioridad es mayor que la mostrada por == y !=
Mayor ">" es una variante estricta
Mayor ">=" es una variante no estricta
'''
Manzanas = 5

print(Manzanas > 5) #False
print(Manzanas >= 5)#True

'''
                                        MENOR O IGUAL QUE
Menor "<" es una variante estricta
Menor "<=" es una variante no estricta
'''
Peras = 6
print(Manzanas < 6) #False
print(Manzanas <= 6)#True

#Se puede almacenar la respuesta
resp = Manzanas < 6