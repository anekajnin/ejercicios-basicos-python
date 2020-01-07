#Crear archivo y añadir contenido
cadena_nueva = '\n- Pues muy bien'
archivo = open('archivo2.txt', 'w')
archivo.write(cadena_nueva)
archivo.write('\nMe alegro')
archivo.close()

archivo = open('archivo2.txt', 'r')
cadena = archivo.read()
print(cadena)
archivo.close()