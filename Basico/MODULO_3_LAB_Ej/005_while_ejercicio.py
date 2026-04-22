counter = 5

#El contador comienza con 5
while counter != 0:
    print("Dentro del bucle.", counter) #imprime el contador
    counter -= 1 #Le resta 1 a cada bucle  que pasa
print("Fuera del bucle.", counter) #sale del bucle cuando counter sea 0

#LEGIBILIDAD
#Son iguales
counter = 5
while counter: #Indica que counter se evaluara como un booleano; 0 = False, 1= True
    #como counter es diferente de 0, se evalua como True (1) y comienza a operar.
    print("Dentro del bucle.", counter)
    counter -= 1
print("Fuera del bucle.", counter)
 