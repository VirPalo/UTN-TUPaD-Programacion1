# Ejercicio 1 ----------
 
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

# Ejercicio 8 ----------

productos = {
    'manzana' : 45,
    'peras' : 33,
    'naranja' : 60,
    'banana' : 55,
    'kiwi' : 25,
    'mandarina' : 28
  }

# Función para Mostrar los productos
def mostrar_productos():
  print('PRODUCTOS EN STOCK:')
  print('PRODUCTO  |  CANTIDAD')
  for i in productos:
    print(f'- {i} | {productos[i]} unidades')  

# Función para Consultar el stock de un producto
def consultar_stock():
  producto = input('Para consultar el stock, ingrese el producto: ').lower()
  if producto in productos:
    print(f'Hay {productos[producto]} unidades en stock.')
  else:
    print('El producto ingresado no existe.')

# Función para Agregar unidades al stock de un producto si existe
def agregar_unidades():
  producto = input('Para ingresar unidades, ingrese el producto: ').lower()
  
  if producto in productos:
    while True:
      cantidad = int(input('Cuantas unidades desea ingresar? '))
      
      if cantidad > 0:
        productos[producto] += cantidad
        print('La cantidad se ha ingresado correctamente.')
        break
      elif cantidad < 0:
        print('Debe ingresar un número entero positivo.')
        
  else:
    print('El producto ingresado no existe.')
    
# Función para Agregar un nuevo producto, si no existe
def agregar_producto():
  producto = input('Para ingresar un nuevo producto, ingrese el nombre del producto: ').lower()
  if producto not in productos:
    productos[producto] = 0
    while True:
      cantidad = int(input('Cuantas unidades desea ingresar? '))
      
      if cantidad > 0:
        productos[producto] += cantidad
        print('Se ha ingresado correctamente.')
        break
      elif cantidad < 0:
        print('Debe ingresar un número entero positivo.')
        
  else:
    print('El producto ingresado ya existe.')

# Llamada a función mostrar_productos
mostrar_productos()

# Llamada a función consultar_stock
consultar_stock()

# Llamada a función agregar_unidades
agregar_unidades()

# Llamada a funcion agregar_producto
agregar_producto()

 
# Ejercicio 9 ----------

agenda = {
  ('lunes','10:00'): 'Reunión',
  ('lunes', '12:00'): 'Almuerzo con cliente',
  ('martes', '15:00'): 'Clase de Inglés',
  ('miercoles', '21:00'): 'Cumpleaños Abuela',
  ('jueves', '12:00'): 'Videollamada',
  ('viernes', '18:00'): 'Turno peluquería'          
}

# Función para mostrar agenda
def mostrar_agenda():
  print('AGENDA:')
  print('DÍA Y HORA  |  ACTIVIDAD')
  for clave in agenda.keys():
    print(f'- {clave[0]} a las {clave[1]}: {agenda[clave]}')  

# Funcion para consultar agenda
def consultar_agenda():
  
  while True:
    dia = input('Para consultar la actividad, ingrese el día (Ejemplo: lunes): ').lower()
    hora = input('Ingrese la hora (Ejemplo: 10:00): ')
    
    if (dia, hora) in agenda.keys():
      print(f'- {dia} a las {hora}: {agenda[(dia, hora)]}')
      break
    else:
      print('Valor inválido o no existe en la agenda. Intente nuevamente.')
    
# Llamada a la función mostrar_agenda
mostrar_agenda()

# Llamada a la función consultar agenda
consultar_agenda()

# Ejercicio 10 ----------

paises = {
  'Argentina':'Ciudad Autónoma de Buenos Aires',
  'Chile': 'Santiago',
  'Uruguay': 'Montevideo',
  'Paraguay': 'Asunción',
  'Brasil': 'Brasilia',
  'Perú': 'Lima',
  'Venezuela': 'Caracas',
  'Colombia': 'Bogotá'
}

# Función para mostrar el diccionario
def mostrar_diccionario(diccionario):
  for i in diccionario:
      print(f'- {i}: {diccionario[i]}')  
      
# Función invertir diccionario
def invertir_diccionario(diccionario):
  invertido = dict()
  for clave, valor in diccionario.items():
    invertido[valor] = clave
  return invertido

# Llamada a la función mostrar diccionario
mostrar_diccionario(paises)

# Llamada a la función mostrar diccionario y luego, mostrar diccionario
capitales = invertir_diccionario(paises)
mostrar_diccionario(capitales)




