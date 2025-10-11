# Ejercicio 1 ----------

# Definición de la función
"""
    
def imprimir_hola_mundo():
    print('Hola Mundo!')

# Programa principal

imprimir_hola_mundo()

# Ejercicio 2 ----------

# Definición de la función

def saludar_usuario(nombre):
    print(f'Hola {nombre}!')

# Programa principal
nombre = input('Ingrese su nombre: ')
saludar_usuario(nombre)

# Ejercicio 3 ----------

# Definición de la función

def informacion_personal(nombre, apellido, edad, residencia):
    print(f'Soy {nombre} {apellido}, tengo {edad} años y vivo en {residencia}.')

# Programa principal
nombre = input('Ingrese su nombre: ')
apellido = input('Ingrese su apellido: ')
edad = int(input('Ingrese su edad: '))
residencia = input('Ingrese su lugar de residencia: ')

informacion_personal(nombre, apellido, edad, residencia)



# Ejercicio 4 ----------

# Definición de la función
import math
def calcular_area_circulo(radio):
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio):
    perimetro = 2 * math.pi * radio
    return perimetro

# Programa principal
print('Para calcular el radio y el perimetro de un circulo debe ingresar el radio.')
radio = int(input('Ingrese el radio: '))

area = calcular_area_circulo(radio)
print(f'El área del círculo es {area}')

perimetro = calcular_perimetro_circulo(radio)
print(f'El perímetro del círculo es {perimetro}')

# Ejercicio 5 ----------

# Definición de la función
def segundos_a_horas(segundos):
    horas = (segundos / 60 ) / 60
    return horas

# Programa principal
segundos = int (input('Ingrese un valor en segundos:'))
horas = segundos_a_horas(segundos)
print(f'El valor {segundos} segundos, corresponde a {horas} hora/s.')

# Ejercicio 6 ----------

# Definición de la función
def tabla_multiplicar(numero):
    print(f'Tabla del {numero}:')
    for i in range(0,11):
        print(f'{numero} x {i} = {i*numero}')        

# Programa principal
numero = int(input('Ingrese un número: '))
tabla_multiplicar(numero)
"""
# Ejercicio 7 ----------

# Definición de la función
def operaciones_basicas(a, b):
    pass
# Programa principal

# Ejercicio 8 ----------

# Definición de la función

# Programa principal

# Ejercicio 9 ----------

# Definición de la función

# Programa principal

# Ejercicio 10 ----------

# Definición de la función

# Programa principal