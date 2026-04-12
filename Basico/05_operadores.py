''' Operadores Basicos
+   -   *   /   //  %   ** '''

#Exponenciación
''' Cuando ambos ** argumentos son enteros, el resultado es entero'''
print("2^2=", 2**2)
print("2^2=",2**3)
print("2^2=",2**4)

'''Cuando al menos un ** argumento es flotante, el resultado también es flotante.'''
print(2 ** 3.)
print(2. ** 3)
print(2. ** 3.,"\n")

#Multiplicación
print(2 * 3)
print(2 * 3.)
print(2. * 3)
print(2. * 3. ,"\n")

#Division
''' El resultado producido por el operador de división siempre es flotante,
sin importar si a primera vista el resultado es flotante: 1 / 2, 
o si parece ser completamente entero: 2 / 1'''
print(6 / 3)
print(6 / 3.)
print(6. / 3)
print(6. / 3.,"\n")

#División entera / floor division.
#Los resultados siempre son redondeados;'
print(6 // 3)
print(6 // 3.)
print(6. // 3)
print(6. // 3.)

''' El resultado de la división entera siempre se redondea al valor entero inferior
mas cercano del resultado de la división no redondeada'''

#¡¡¡¡¡ PUEDE SER UN PROBLEMA CUANDO LOS RESULTADOS NO SON ENTEROS: !!!!!

#EJEMPLO1:
print(6 // 4) #El resultado correcto deberia ser: 1.5 
# Sin embargo el resultado que se imprime es -----> 1

print(6. // 4) # 6./4 =1.5 ----->  # 6.//4 =1.0


#EJEMPLO2: 
'''El redondeo siempre va hacia abajo.'''
print(-6 // 4) #El resultado correcto deberia ser:  -1.5 
# Sin embargo el resultado que se imprime es ----->  -2

print(6. // -4) # 6./-4 =-1.5 ----->  # 6.//-4 =-2.0

#Residuo (módulo)
''' Es el valor que sobra después de dividir un valor entre otro para
producir un resultado entero.'''
print(14 % 4) # =2
print(12 % 4.5) # = 3.0

#SUMA
print(-4 + 4)
print(-4. + 8)

#RESTA
print(-1.1)
print(-4 - 4)
print(-4 - -4)
print(4. - 8)

#Es asociativo por la derecha, no por la izquierda.
print(2 ** 3 ** 2) # ---->  (2 ** (3 ** 2)) = (2 ** 9)

