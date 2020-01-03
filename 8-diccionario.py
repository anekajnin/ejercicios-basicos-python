#En un diccionario podemos almacenar todo tipo de datos.
#Lo que lo hace diferente a una lista o una tupla es que no tenemos índice.
#No podemos modificar los valores mediante índice. Para poder realizar esas
#acciones hay que crear una clave.

#diccionario = { 55 }
#Así no se puede asignar, hay que crear una clave: 

diccionario = { 'a' : 55 }
print (diccionario)

#Podemos usar string como llaves y también números
#Las claves deben ser inmutables
diccionario1 = { 'a' : 55 , 1 : "Esto es un string con clave 1" , (1,2) : False }
print (diccionario1)

#Si repito la clave, se quedará con el último valor (el de más a la derecha)
#PODEMOS REPETIR LAS LLAVES PERO EL VALOR SERÁ EL ÚLTIMO
diccionario2 = { 'a' : 55 , 1 : "Esto es un string con clave 1" , (1,2) : False , 'a' : 1}
print (diccionario2)

diccionario2 = { 'a' : 55 , 1 : "Esto es un string con clave 1" , (1,2) : False , 'a' : 1 , 'a' : 2}
print (diccionario2)

#AÑADIR UN VALOR (SI NO ESTÁ) | ACTUALIZAR VALOR (SI ESTÁ)
diccionario2['c'] = 'nuevo string' #Creamos Clave/Valor
diccionario2['a'] = False
print(diccionario2)

#OBTENER UN VALOR DEL DICCIONARIO POR UNA CLAVE
valor = diccionario2['c']
print(valor)
#Si la clave NO EXISTE --> ERROR

#Lo suyo es usar get:
valor = diccionario.get('aa', "No la encontré!") 
print(valor)

#BORRAR
print("\n\n")
print(diccionario2)
del diccionario2['c']
print(diccionario2)

#Keys nos devuelve un objeto iterable donde estarán todas las llaves
llaves = diccionario2.keys()
print(llaves)

#Si quisiera convertirlo en lista pura podría hacer esto:
llaves = list(diccionario2.keys())
print(llaves)

#Obtejer los valores de los diccionarios
valores = diccionario2.values()
print(valores)
valores = list(diccionario2.values())
print(valores)