
#La función input() es capaz de leer datos que fueron introducidos por el usuario
print("Dime lo que sea...")
anything = input()
print("Hmm...", anything, "... ¿en serio?")

#Ejemplo1:
print("Edad Actual?")
edad = input()
print("Asi que tu edad es:", edad)

#La función input() con un argumento
#La función input() puede hacer otra cosa: 
# puede avisar al usuario sin ninguna ayuda de print().
edad = input("Edad Actual?")
print("Asi que tu edad es:", edad)


#la función input() puede ser utilizada para pedirle al usuario que termine o finalice
# el programa.
name = input("Ingresa tu nombre: ")
print("Hola, " + name + ". '¡Gusto en conocerte'!")
print("\nPresiona Enter para terminar el programa.")
input()
print("FIN.")

#EJEMPLO: ERROR!!!!!!
## Probando un mensaje de error TypeError.
#El resultado de la función input() es una cadena.
#No se debe utilizar como un argumento para operaciones matemáticas
anything = input("Ingresa un número:")
something = anything ** 2.0
print(anything, "al cuadrado es", something)