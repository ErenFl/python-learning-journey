        #Contando lentamente (mississippily)
        
'''Tu tarea es muy simple aquí: escribe un programa que use un bucle for para 
"contar de forma mississippi" hasta cinco. Habiendo contado hasta cinco, el programa
debería imprimir en la pantalla el mensaje final "¡Listos o no, ahí voy!" '''

import time

# Escribe un bucle for que cuente hasta cinco.
    # Cuerpo del bucle: imprime el número de iteración del bucle y la palabra "Mississippi".
    # Cuerpo del bucle, emplea : time.sleep(1)

for i in range(1,6):
    print(i, "mississippi")
    time.sleep(1)
    
# Escribe una función print con el mensaje final.
print("¡Listos o no, ahí voy!")


