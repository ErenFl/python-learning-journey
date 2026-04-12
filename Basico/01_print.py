'''print() es una función integrada 
imprime/envía un mensaje específico a la pantalla/ventana de consola.


Las funciones integradas, al contrario de las funciones definidas por el usuario,
están siempre disponibles y no tienen que ser importadas.
'''

#INVOCACION DE LA FUNCION

#Invocación vacia de la funcion print()
print("Dijo que yo era raro, que me amaba por eso")
print()
print("Pero yo sé que un día me odiara por las mismas razonez")

#Carácter de escape.
'''
El carácter (\ n) llamado "newline" insta a la consola a iniciar una nuevalínea de salida.
'''
print("\nDijo que yo era raro,\n que me amaba por eso")
print()
print("Pero yo sé que un día \nme odiara por las mismas razones")

#Tiene dos concecuencias:
'''Incorrecto ---->''' # print("\")

'''Correcto ---->''' 
print("\\")

#Tambien se usa cuando:
'''Incorrecto ---->''' #print("Hola me llamo "Juan Martinez"")
'''Correcto ---->''' 
print("Hola me llamo \"Juan Martinez\"")
print("Hola me llamo 'Juan Martinez'")
print("Hola me llamo Juan\'s Martinez")


#Usando múltiples argumentos
print("Hola","como","te fue hoy") 

#Argumentos de palabras clave
#Los argumentos de palabras clave deben colocarse al final del argumento posicional

    #end
print("Mi sueño es...", end=" ")
print("¡La paz en el mundo entero!")
print()
    #sep
print("Que","vamos", "a", "hacer", "hoy?", sep=" ")
print("Que","vamos", "a", "hacer", "hoy?", sep="-")

print("Que","vamos", "a", "hacer", "hoy?", sep="*", end="_")
print("Conquistar", "el", "mundo", sep="/", end="\n")


print("Programming","Essentials","in", sep="***", end="...")
print("Python")

