'''
elif se usa para verificar más de una condición, 
y para detener cuando se encuentra la primera sentencia verdadera.

if the_weather_is_good:
    go_for_a_walk()
elif tickets_are_available:
    go_to_the_theater()
elif table_is_available:
    go_for_lunch()
else:
    play_chess_at_home()
    
'''
buen_clima = input("Hoy hay un buen clima (Si/No)")
if buen_clima == "Si":
    print("salir a caminar")
elif input("Tienes boletos de cine (Si/No)?")== "Si":
    print("Ir al cine")
elif input("Tienes mesa reservada (Si/No)?")== "Si":
    print("Ir a comer")
else: #Ultima rama de la cascada
    print("Jugar_ajedrez en casa")