# Ejercicio 1
'''

notas = [10, 9.3, 5.5, 7, 8.5, 10, 8, 9.5, 1, 4]
suma = 0
nota_alta = 0
nota_baja = 10

for nota in notas:
    print(nota)
    suma += nota
    if nota > nota_alta:
        nota_alta = nota
    elif nota < nota_baja:
        nota_baja = nota 

promedio = suma / len(notas)
print('El promedio de las notas es', promedio)
print(f'La nota más alta es {nota_alta} y la nota más baja es {nota_baja}.')

# Ejercicio 2

productos = []

for i in range(5):
    producto = input(f'Ingrese el producto {i+1}\n')
    productos.append(producto.lower())

productos_ordenados = sorted(productos)
print(productos_ordenados)

print('Si desea eliminar un producto presione 1, sino presione 0.')
opc = int(input())

if opc == 1:
    print('Qué producto desea eliminar?')
    prod_eliminar = input()
    productos_ordenados.remove(prod_eliminar.lower())
    print('La lista final de productos es la siguiente :', productos_ordenados)
elif opc == 0:
    print('Programa finalizado.')
else:
    print('Ha ingresado un valor incorrecto.')


# Ejercicio 3
import random

lista = []

for i in range(15):
    num = random.randint(0, 100)
    lista.append(num)

print(f'La lista generada al azar es {lista}')

lista_pares = []
lista_impares = []

for i in lista:
    if i % 2 == 0:
        lista_pares.append(i)
    elif i % 2 == 1:
        lista_impares.append(i)

print(f'Los numeros impares de la lista son {len(lista_impares)} y son los siguientes {lista_impares}.')
print(f'Los numeros pares de la lista son {len(lista_pares)} y son los siguientes {lista_pares}.')


# Ejercicio 4

#datos = [1, 3, 5, 3, 7, 1, 9, 5, 3]

#for i in range(len(datos)):
#TERMINAR!!   
    
# Ejercicio 5

estudiantes = ['marcela', 'patricia', 'virginia', 'jose', 'juan', 'bautista', 'facundo', 'lorena']
print('La lista de estudiantes presentes es :', estudiantes)

print('\nElija una de las siguientes opciones:')
print('1 - Agregar un nuevo estudiante.')
print('2 - Eliminar un estudiante existente.')
print('0 - Salir.')
opc = int(input())

if opc == 1:
    estudiante = input('Ingrese el nombre del estudiante a incorporar\n')
    estudiantes.append(estudiante)
    print('La lista final es ', estudiantes)
elif opc == 2:
    estudiante = input('Ingrese el nombre del estudiante a eliminar\n')
    estudiantes.remove(estudiante.lower())
    print('La lista final es ', estudiantes)
elif opc == 0:
    print('El programa ha finalizado.')
else:
    print('El valor ingresado no es correcto.')

# Ejercicio 6

numeros = [5, 80, 24, 32, 7, 12, 98, 65]
print(numeros)

ultimo = numeros.pop()
numeros.insert(0, ultimo)
    
print(numeros)

# Ejercicio 7

temperaturas = [
    [10, 24],
    [12, 24],
    [11, 21],
    [7, 24],
    [10, 24],
    [12, 23],
    [11, 22],
]
# Se calculan los promedios de temperaturas maximas y minimas

suma_min = 0
suma_max = 0

for i in temperaturas:
    suma_min += i[0]
    suma_max += i[1]

prom_min = suma_min / len(temperaturas)
prom_max = suma_max / len(temperaturas)

print(f'El promedio de las temperaturas bajas es {prom_min:.2f}°C.') # :.2f Me tira el promedio solo con dos decimales(redondea).
print(f'El promedio de las temperaturas altas es {prom_max:.2f}°C.')

# Se calcula la maxima amplitud termica y el dia en que se da.

amplitud_max = 0
dia_max_amplitud = -1

for i, dia in enumerate(temperaturas): # Con funcion enumerate() recorro la lista y me traigo el indice.
    amplitud = dia[1] - dia[0]
    if amplitud > amplitud_max:
        amplitud_max = amplitud
        dia_max_amplitud = i

print(f'La amplitud máxima es de {amplitud_max} grados y se da en el día {dia_max_amplitud}.') 
'''

# Ejercicio 8

notas = [
    
]

# Ejercicio 9

# Ejercicio 10

