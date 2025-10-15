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

# Ejercicio 4 ----------

contactos = dict()

for i in range(1,6):
    # El usuario ingresa los datos
    nombre = input(f'Ingrese el nombre del contacto {i}: ')
    numero = int(input('Ahora, ingrese el número de teléfono: '))
    
    # Valido que la clave sea unica
    while nombre in contactos.keys():
      print('El nombre ya existe. Intente nuevamente')
      nombre = input(f'Ingrese el nombre del contacto {i}: ')
      numero = int(input('Ahora, ingrese el número de teléfono: '))
        
    contactos[nombre] = numero

print(contactos)

nombre_pedido = input('Ingrese un nombre para mostrar el número de telefono asociado: ')
if nombre_pedido in contactos.keys():
  print(f'El número de {nombre_pedido} es {contactos[nombre_pedido]}')
else:
  print('El nombre no existe.')
   
# Ejercicio 5 ----------

frase = input('Ingrese una frase: ')

palabras_set = set(frase.split())
print(palabras_set)

palabras = frase.split()
recuento = dict()

for palabra in palabras:
  palabra_unica = palabra.lower()
  if palabra_unica in recuento:
    recuento[palabra_unica] += 1
  else:
    recuento[palabra_unica] = 1
  
print(recuento)
''' 
# Ejercicio 6 ----------

alumnos = dict()

for i in range(3):
  nombre = input(f'Ingrese el nombre del alumno/a {i+1}: ')
  print(f'Ahora ingrese las notas del alumno/a {nombre}')
  
  for j in range(3):
    notas = list()
    nota = float(input(f'Ingrese la nota {j+1}: '))
    notas.append(nota)
  
  #notas = tuple(notas)
  alumnos[nombre] = notas

print(alumnos)



# Ejercicio 7 ----------
# Ejercicio 8 ----------
# Ejercicio 9 ----------
# Ejercicio 10 ----------

