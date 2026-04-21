            #Bucles con for
            
#En este caso, la función range() comienza su trabajo desde 0 
# y lo finaliza un número entero) antes del valor de su argumento.
'''for i in range(100):     /// range() solo acepta enteros como argumentos 
    # do_something()
    pass '''

    #Ejemplo1
for i in range(10):
    print("El valor de i es", i) #imprime desde el 0 al 9
    
    #Ejemplo2
for i in range(2, 8): #El segundo argumento le dice a la función dónde detener la secuencia
    print("El valor de i es", i) #Inicia el conteo desde el "2" y lo termina en "7"+

    #Ejemplo3
for i in range(2, 8, 3): #El tercer argumento es un incremento (3)
    print("El valor de i es", i) #Incrementa en 3 el valor inicial, 2, (2+3)=5, (5+3)=8...
 
 
 
''' El conjunto generado por range() debe ordenarse en un orden ascendente. 
 No hay forma de forzar el range() para crear un conjunto en una forma diferente. 
 Esto significa que el segundo argumento de range() debe ser mayor que el primero. '''
 
    #Ejemplo_ERROR_1
for i in range(1, 1): #El {rango final}, no puede ser menor que el {rango inicial}
    print("El valor de i es", i)
    
    #Ejemplo_ERROR_2
for i in range(2, 1): #El {rango final} debe ser mayor al inicial
    print("El valor de i es", i)

