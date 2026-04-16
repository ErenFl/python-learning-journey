#El signo de + (más), al ser aplicado a dos cadenas
# se convierte en un operador de concatenación
            #string + string

nomb = input("¿Me puedes dar tu nombre por favor? ")
apell = input("¿Me puedes dar tu apellido por favor? ")
print("Gracias. ")
print("\nTu nombre es " + nomb + " " + apell + ".")


#Replicación
#El signo de * (asterisco), cuando es aplicado a una cadena y a un número 
# (o a un número y cadena) se convierte en un operador de replicación
            #string * number
            #number * string
'''Replica la cadena el numero de veces indicado por el número.
Por ejemplo:

"James" * 3 produce "JamesJamesJames"
3 * "an" produce "ananan"
5 * "2" (o "2" * 5) produce "22222" (no 10!) '''

print("+" + 10 * "-" + "+")  #  +----------+
print(("|" + " " * 10 + "|\n") * 5, end="")
print("+" + 10 * "-" + "+")