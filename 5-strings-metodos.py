curso = 'Curso'
cadena = 'Código Facilito'

""" Strings: Formato """

result = '{} de {}'.format(curso, cadena)
print(result)

result = '{a} de {b}'.format(b = curso, a = cadena)
print(result)

result = result.lower()
print(result)

result = result.upper()
print(result)

#La primera letra mayúscula
result = result.title()
print(result)

""" Strings: Búsquedas """

pos = result.find('Facilito')
print(pos)
#Devuelve la posición inicial de Facilito (7).
print(result[7])

#Contar cuantas veces se repite un caracter/cadena dentro de una cadena
contador = result.count('Có')
print(contador)

#Sustitución
cadena_nueva = result.replace('Có', 'x')
print(cadena_nueva)

#Dividir una cadena en bloques
cadena_nueva_dos = result.split(' ') #Dividir en espacios
print(cadena_nueva_dos)
