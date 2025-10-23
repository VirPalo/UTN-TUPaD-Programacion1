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

# Ejercicio 6 ----------

alumnos = dict()

for i in range(3):
  #El usuario ingresa el nombre del alumno/a
  nombre = input(f'Ingrese el nombre del alumno/a {i+1}: ')
  print(f'Ahora ingrese las notas del alumno/a {nombre}')
  
  #El usuario ingresa cada nota y la guardo en una lista
  # En el mismo bucle calculo el promedio
  notas = list()
  promedio = 0
  for j in range(3):
    nota = float(input(f'Ingrese la nota {j+1}: '))
    notas.append(nota)
    promedio += nota
    
  #Muestro el promedio
  print(f'El promedio de {nombre} es {(promedio / 3):.2f}.')
    
  #Convierto la lista a tupla y la guardo en el diccionario
  notas = tuple(notas)
  alumnos[nombre] = notas
  
# Ejercicio 7 ----------

p1 = {1000, 1010, 1003, 1011, 1012, 1014, 1025, 1033}
p2 = {1000, 1001, 1002, 1003, 1005, 1011, 1013, 1033}

# Alumnos que aprobaron ambos parciales
ambos = list()

ambos = p1.intersection(p2) # Los valores que estan en los dos conjuntos 
print(f'Los alumnos que aprobaron los dos parciales son: {ambos}.')

# Alumnos que aprobaron solo uno de los parciales
solo_uno = list()

solo_uno = p1.symmetric_difference(p2) # Dif simetrica: Los valores que estan en uno u otro conjunto pero no en ambos.
print(f'Los alumnos que aprobaron solo uno de los dos parciales son: {solo_uno}.')

# Alumnos que aprobaron al menos uno de los parciales
al_menos_uno = list()

al_menos_uno = p1.union(p2) # Todos los valores de ambos conjuntos
print(f'Los alumnos que aprobaron al menos uno de los dos parciales son: {al_menos_uno}.')
''' 
# Ejercicio 8 ----------

#productos = dict()

# Ejercicio 9 ----------

agenda = {
  ('lunes','10:00'): 'Reunión',
  ('lunes', '12:00'): 'Almuerzo con cliente',
  ('martes', '15:00'): 'Clase de Inglés',
  ('miercoles', '21:00'): 'Cumpleaños Abuela',
  ('jueves', '12:00'): 'Videollamada',
  ('viernes', '18:00'): 'Turno peluquería'          
}

print()

# Ejercicio 10 ----------

