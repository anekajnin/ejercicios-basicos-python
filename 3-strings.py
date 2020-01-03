my_string = "Hola Mundo!"
my_string_2 = 'Hola Mundo!'
my_string_3 = "Hola 'Patri'"

print (my_string)
print (my_string_2)
print (my_string_3)

#Saltos de línea. Se usa la comilla doble o la simple 3 VECES
my_string_4 = """Este string 
contiene saltos
de linea """
print(my_string_4)

my_string_5 = '''Este es otro
salto
de línea. Mira que chulo :D'''
print(my_string_5)

#Podemos maquetar con \n.
my_string_6 = """\n\nEste string\ncontiene saltos\nde línea """
print(my_string_6)

#Los string son inmutables, si hago un replace la 
#cadena original NO se modifica, 
#pero la función devuelve una cadena modificada.
logico = my_string_4.replace('n', '3')
print(my_string_4)
print("\nCadena modificada:\n", logico, "\n")

#Concatenar cadenas
#Forma 1
curso = "Curso de"
tematica = "Python"
nombre_curso_entero = "NUEVO: " + curso + " " + tematica
print (nombre_curso_entero)

#Concatenar cadenas
#Forma 2
nombre_curso_entero = "NUEVO: %s %s" %(curso, tematica)
print(nombre_curso_entero)

#Concatenar cadenas
#Forma 3
nombre_curso_entero = "NUEVO: {} {}".format(curso, tematica)
print(nombre_curso_entero)
#En este caso se ha llamado al método/función format de la clase String.

