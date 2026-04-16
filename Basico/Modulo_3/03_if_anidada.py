
el_tiempo_es_bueno = input("El tiempo es bueno?")
se_encuentra_un_restaurante_bonito = input("Encontraste un restaurante bonito? ")
las_entradas_están_disponibles = input("Entradas disponibles?")

if el_tiempo_es_bueno == True: 
    if se_encuentra_un_restaurante_bonito == True: 
        print("Almorzar")
    else:  
        print("comer_un_sándwich")
else: 
    if las_entradas_están_disponibles == True: 
        print("Ir_al_teatro") 
    else:
        print("ir de compras")