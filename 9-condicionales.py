#CONDICIONES: > < >= <= != ==

"""
fruta = 'manzana'

if fruta == 'kiwi':
    print('El valor es kiwi')
else:
    print("No es un kiwi")

mensaje = 'El valor es kiwi' if fruta == 'kiwi' else 'No es un kiwi'
print (mensaje)

if fruta == 'kiwi':
    print('El valor es kiwi')
elif fruta == 'manzana':
    print('El valor es manzana')
elif fruta == 'plátano':
    pass
else:
    print("No es un kiwi")

#True  = 1
#False = 0

if 1: #Es lo mismo que: if True:
    print("hola!!")
    
valor = 0 #None, False, [], {}, ()

if valor:
    print(valor)
else: 
    print("valor está vacío")

"""

valor = 1
valor_dos = 21

if valor and valor_dos > 20: 
    print ("Valor es verdadero y valor_dos mayor que 20")
    
    
if valor or valor_dos > 20: #or o |
    print ("Valor es verdadero o valor_dor mayor que 2")