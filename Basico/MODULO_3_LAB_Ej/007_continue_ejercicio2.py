            #La sentencia continue – el Feo Devorador de Vocales
'''
Tu tarea aquí es muy especial: ¡Debes diseñar un devorador de vocales!. Escribe un programa que use:
un bucle for;
el concepto de ejecución condicional (if-elif-else).
la sentencia continue.

Tu programa debe:
-pedir al usuario que ingrese una palabra.
-utiliza user_word = user_word.upper() para convertir la palabra ingresada por el usuario 
a mayúsculas;
-utiliza la ejecución condicional y la instrucción continue para "devorar" las siguientes 
vocales A, E, I, O, U de la palabra ingresada.
imprime las letras no consumidas en la pantalla, cada una de ellas en una línea separada'''
    
# Indicar al usuario que ingrese una palabra
# y asignarlo a la variable user_word.

user_word = input("Ingresa una palabra: ")
user_word = user_word.upper()  #indicamos ue upper es una cadena con ()

for letter in user_word:
    # Completa el cuerpo del bucle for.
    if letter == "A":
        continue
    elif letter == "E":
        continue
    elif letter == "I":
        continue
    elif letter == "O":
        continue
    elif letter == "U":
        continue
    else:
        print(letter) #Imprime letra por letra despues de compararla con todas las vocales
        #print() dentro del for → imprime muchas líneas
    #Al tener un resultado falso se ejecuta el else:
    
    '''
    letra = "M"
    
    "M" == "A" → False
    "M" == "E" → False
    "M" == "I" → False
    "M" == "O" → False
    "M" == "U" → False
    
    else → print("M")
    '''
    
    

