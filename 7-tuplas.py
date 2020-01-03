#Nos van a permitir usar cualquier tipo de datos. Son inmutables, no como las listas. 
#No puedo agregar ni quitar elementos
#Vamos a usarla siempre que esos datos vayan a ser constantes
#Ej: Inicializar un servidor, password de una BBDD, ...

mi_tupla = (1, "string", True)
print(mi_tupla)

#Podemos entrar a un índice concreto
print(mi_tupla[1])
print(mi_tupla[0:2])