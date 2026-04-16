'''

if true_or_not:
    do_this_if_true
    
    
-La palabra clave reservada if;
-Uno o más espacios en blanco;
-Una expresión (una pregunta o una respuesta) cuyo valor se interpretar únicamente en
términos de True (cuando su valor no sea cero) y False (cuando sea igual a cero);
-Unos dos puntos seguidos de una nuevalínea;
-Una instrucción con sangría o un conjunto de instrucciones.

¡¡Es importante que todas las sangrías sean exactamente iguales 
Python 3 no permite mezclar espacios y tabuladores para la sangría!!!

'''

#Ejemplo:

Ovejas = int(input("Cuantas ovejas haz contado? "))

if Ovejas >= 120: # Evaluar una expresión condicional
    print("Duerme y sueña") # Ejecutar si la expresión condicional es verdadera
else: 
    print("Segue contando") # Ejecutar si la expresión condicional es falsa


