# Ejercicio 1 ----------
''' 
#Defino el diccionario
precios_frutas = {'Banana': 1200, 'Ananá': 2500, 'Melón': 3000, 'Uva': 1450}

print(precios_frutas)

#Añado pares de clave-valor
precios_frutas ['Naranja'] = 1200
precios_frutas ['Manzana'] = 1500
precios_frutas ['Pera'] = 2300

print(precios_frutas)

# Ejercicio 2 ----------

# Actualizar valores del diccionario precios_frutas
precios_frutas ['Banana'] = 1330
precios_frutas ['Manzana'] = 1700
precios_frutas ['Melón'] = 2800

print(precios_frutas)

# Ejercicio 3 ----------

# Lista con las keys del diccionario anterior
lista_frutas = list(precios_frutas.keys())

print(lista_frutas)
'''
# Ejercicio 4 ----------

contactos = {}

for i in range(1,6):
    # El usuario ingresa los datos
    nombre = input(f'Ingrese el nombre del contacto {i}: ')
    numero = int(input('Ahora, ingrese el número de teléfono: '))
    
    # Valido que la clave sea unica
    #while nombre in contactos.keys():
     #   print('El nombre ya existe.')
      #  nombre = input('Ingrese un nombre nuevamente: ')
        
    contactos[nombre] = numero

print(contactos)
    
    
# Ejercicio 5 ----------
# Ejercicio 6 ----------
# Ejercicio 7 ----------
# Ejercicio 8 ----------
# Ejercicio 9 ----------
# Ejercicio 10 ----------

