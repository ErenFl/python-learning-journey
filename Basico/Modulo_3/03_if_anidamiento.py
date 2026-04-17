#Sentencias if-else anidadas

el_tiempo_es_bueno = input("El tiempo es bueno (Si/No)?")

if el_tiempo_es_bueno == "Si": #Comparar cadenas ""
    se_encuentra_un_restaurante_bonito = input("Encontraste un restaurante bonito (Si/No)? ")
    if se_encuentra_un_restaurante_bonito == "Si": 
        print("Almorzar")
    else:  
        print("Comer un sándwich")
else: 
    las_entradas_están_disponibles = input("Entradas disponibles (Si/No)?")
    if las_entradas_están_disponibles == "Si": 
        print("Ir al teatro") 
    else:
        print("Ir de compras")