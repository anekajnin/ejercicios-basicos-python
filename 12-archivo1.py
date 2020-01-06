#Crear o abrir un archivo si existe
contenido = 'Hola, ¿qué tal?'
archivo = open('archivo1.txt', 'w')

#Escribir contenido
archivo.write(contenido)
archivo.close

#Leer contenido
archivo = open('archivo1.txt', 'r')
cadena = archivo.read()
#print(cadena)
archivo.close()

#Añadir contenido
cadena_nueva = '\n- Pues muy bien'
archivo = open('archivo1.txt', 'a')
archivo.write(cadena_nueva)
archivo.close()

archivo = open('archivo1.txt', 'r')
cadena = archivo.read()
print(cadena)
archivo.close()