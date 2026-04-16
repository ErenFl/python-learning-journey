#La función int() toma un argumento (por ejemplo, una cadena: int(string))
# e intenta convertirlo a un valor entero;
altura = int(input("Dame la altura "))
base = int(input("Dame la base "))
area_triangulo =(base*altura) / 2
print("El area del triangulo es: ", area_triangulo)


#La función float() toma un argumento (por ejemplo, una cadena: float(string))
#e intenta convertirlo a flotante
anything = float(input("Ingresa un número: "))
something = anything ** 2.0
print(anything, "a la potencia de 2 es", something)

#También se puede convertir un numero a una cadena
#str() -----------> str(number)
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es " + str((leg_a**2 + leg_b**2) ** .5))



#EJEMPLO 3:
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
hypo = (leg_a**2 + leg_b**2) ** .5
print("La longitud de la hipotenusa es:", hypo)

#Tambien podemos quitar hypo ya que la función print() acepta una expresión como argumento
leg_a = float(input("Ingresa la longitud del primer cateto: "))
leg_b = float(input("Ingresa la longitud del segundo cateto: "))
print("La longitud de la hipotenusa es:", (leg_a**2 + leg_b**2) ** .5)
