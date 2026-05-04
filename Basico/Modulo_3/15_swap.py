#Python ofrece una forma más conveniente de hacer un intercambio
'''Forma erronea
variable_1 = 1
variable_2 = 2
 
variable_2 = variable_1
variable_1 = variable_2

¡¡ Si hacemos esto, se perdera el valor previamente almacenado en variable_2

'''

#Forma correcta
variable_1 = 1
variable_2 = 2
 
auxiliary = variable_1
variable_1 = variable_2
variable_2 = auxiliary

#FORMA MAS CONVENIENTE!!!
variable_1, variable_2 = variable_2, variable_1


#EJEMPLO 1
my_list = [10, 1, 8, 3, 5]
 
my_list[0], my_list[4] = my_list[4], my_list[0]
my_list[1], my_list[3] = my_list[3], my_list[1]
 
print(my_list)

#PARA MAS VALORES ----> FOR
length = len(my_list) #Faltaba definirlo

for i in range(length // 2):
    my_list[i], my_list[length - i - 1] = my_list[length - i - 1], my_list[i]

print(my_list)

