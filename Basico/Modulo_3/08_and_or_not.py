#Lógica de computadoras
''' AND Depende del cumplimiento simultaneo de dos condiciones 
se le denomina CONJUNCION, Es un operador binario '''

#counter > 0 and value == 100

''' OR Depende del cumplimiento de al menos una de las condiciones.
se le denomina DISYUNCION. Es un operador binario '''

''' NOT  es un operador unario que realiza una negación lógica.
Convierte lo verdadero en falso, y lo falso en verdad '''

#Ejercicio 1
var = 1
print(var < 0) #False
print(not(var <= 0)) #True

print(var != 0) #True
print(not(var == 0)) #True


#Ejercicio 2
'''
not(p and q) == (not p) or (not q)
not (p or q) == (not p) and (not q)
'''