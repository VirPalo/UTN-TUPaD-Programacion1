# Ejercicio 1 ----------

# Lista para agregar los 3 productos juntos al .txt
lineas = [
    'Taza blanca,4500,10\n',
    'Copa,10000,12\n',
    'Ensaladera,7500,8\n',
]

# Con with, escribo el archivo productos.txt
with open('productos.txt', 'w') as productos:
    productos.writelines(lineas)
 
# Ejercicio 2 ----------

# Abro el archivo con with, solo lectura
with open('productos.txt', 'r') as archivo:
    for linea in archivo:
        linea = linea.strip() # Ignoro los espacios
        columna = linea.split(',') # Divido la linea en una lista
        print(f'Producto: {columna[0]} | Precio: ${columna[1]} | Cantidad: {columna[2]}')

# Ejercicio 3 ----------

# Pido al usuario el nuevo producto
print('Para ingresar un nuevo producto')
prod = input('Ingrese el nombre del producto: ')
precio = input('Ingrese el precio del producto: ')
cant = input('Ingrese la cantidad del producto: ')
producto = prod + ',' + precio + ',' + cant

with open('productos.txt', 'a') as archivo:
    archivo.writelines(producto)

# Ejercicio 4 ----------

with open('productos.txt', 'r') as archivo:
    productos = list()
    for linea in archivo:
        columna = linea.strip().split(',')
        productos.append({'nombre': columna[0], 'precio': columna[1], 'cantidad': columna[2]})
    print(productos)
    
# Ejercicio 5 ----------

nombre_ingresado = input('Para buscar un producto, ingrese su nombre: ')
encontrado = False
for producto in productos:
    if nombre_ingresado.lower() == producto['nombre'].lower():
        print(producto)
        encontrado = True

if not encontrado:
    print('El producto no existe.')
        
# Ejercicio 6 ----------

# Funcion para guardar los productos en el archivo
def guardar_productos(productos):
    with open('productos.txt', 'w') as archivo:
        for producto in productos:
            nombre = producto['nombre']
            precio = producto['precio']
            cantidad = producto['cantidad']
            
            linea = nombre + ',' + str(precio) + ',' + str(cantidad) + '\n'
            archivo.write(linea)

# Llamada a la funcion
guardar_productos(productos)
print('Archivo guardado correctamente.')
        
    