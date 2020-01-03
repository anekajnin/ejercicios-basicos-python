#Las listas pueden almacenar diferentes tipos de datos
#y pueden modificar su tamaño. 

lista = ["strings", 15, 15.6, True]
print (lista)

#AGREGAR DATOS
lista.append(6) #Lo añade al final de la lista
print (lista)

#AGREGAR DATOS EN UNA POSICIÓN ESPECÍFICA
lista.insert(0, "insert")
print (lista)

#Todo lo que vimos en los STRINGS puede aplicarse a las listas
#BORRAR DATOS
lista.remove(15)
print (lista)

ultimo_valor = lista.pop() #Saca el último valor de la lista
print (lista)
print(ultimo_valor)

#También podemos tener listas de un solo valor (lógicamente)
lista_enteros = [10,21,55,69,96,15]
print (lista_enteros)

#Ordenar lista de forma ascendente
lista_enteros.sort()
print (lista_enteros)

#Ordenar lista de forma descendente
lista_enteros.sort(reverse = True)
print (lista_enteros)

#Unir listas
lista_aux = [22, 23] 
lista_enteros.extend(lista_aux)
print(lista_enteros)

#ALMACENAR UNA LISTA DENTRO DE OTRA --> APPEND
lista_aux = [22, 23] 
lista_enteros.append(lista_aux)
print(lista_enteros)