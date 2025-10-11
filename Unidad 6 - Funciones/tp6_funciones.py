# Ejercicio 1 ----------

# Definición de la función
def imprimir_hola_mundo(): # Saludar
    print('Hola Mundo!')

# Programa principal

imprimir_hola_mundo()

# Ejercicio 2 ----------

# Definición de la función
def saludar_usuario(nombre): # Saludar con nombre
    print(f'Hola {nombre}!')

# Programa principal
nombre = input('Ingrese su nombre: ')
saludar_usuario(nombre)

# Ejercicio 3 ----------

# Definición de la función
def informacion_personal(nombre, apellido, edad, residencia): # Mostrar informacion personal
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
def calcular_area_circulo(radio): # Calcular radio de un circulo
    area = math.pi * (radio ** 2)
    return area

def calcular_perimetro_circulo(radio): # Calcular perimetro de un circulo
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
def segundos_a_horas(segundos): # Convertir segundos a horas
    horas = (segundos / 60 ) / 60
    return horas

# Programa principal
segundos = int (input('Ingrese un valor en segundos:'))
horas = segundos_a_horas(segundos)
print(f'El valor {segundos} segundos, corresponde a {horas} hora/s.')

# Ejercicio 6 ----------

# Definición de la función
def tabla_multiplicar(numero): # Mostrar la tabla de multipl de un numero
    print(f'Tabla del {numero}:')
    for i in range(0,11):
        print(f'{numero} x {i} = {i*numero}')        

# Programa principal
numero = int(input('Ingrese un número: '))
tabla_multiplicar(numero)

# Ejercicio 7 ----------

# Definición de la función
def operaciones_basicas(a, b): # Sumar, restar, multip y dividir 2 valores
    suma = a + b
    resta = a - b
    multiplicacion = a * b
    division = a / b
    return (suma, resta, multiplicacion, division)
    
# Programa principal
a = int(input('Ingrese el primer numero: '))
b = int(input('Ingrese el segundo numero: '))

resultados = operaciones_basicas(a, b)

print(f'La suma es {a} + {b} = {resultados[0]}')
print(f'La resta es {a} - {b} = {resultados[1]}')
print(f'La multiplicación es {a} * {b} = {resultados[2]}')
print(f'La división es {a} / {b} = {resultados[3]}')

# Ejercicio 8 ----------

# Definición de la función
def calcular_imc(peso, altura): # Calcular indice de masa corporal
    imc = peso / altura
    return imc

# Programa principal
peso = float(input('Ingrese su peso en kilogramos: '))
altura = float(input('Ingrese su altura en metros: '))

imc = calcular_imc(peso, altura)
print(f'Su índice de masa corporal es {round(imc, 2)}.')

# Ejercicio 9 ----------

# Definición de la función
def celsius_a_fahrenheit(tc): # Convertir temperatura de grados Celsius a grados Farenheit
    tf = (tc * 9/5) + 32
    return tf

# Programa principal
tc = float (input('Ingrese la temperatura en grados Celsius: '))
tf = celsius_a_fahrenheit(tc)
print(f'La temperatura en grados Farenheit es {tf}°F.')

# Ejercicio 10 ----------

# Definición de la función
def calcular_promedio(a, b, c): # Calcular promedio entre 3 valores
    prom = (a + b + c) / 3
    return prom

# Programa principal
a = float(input('Ingrese el primer numero: '))
b = float(input('Ingrese el segundo numero: '))
c = float(input('Ingrese el tercer numero: '))

prom = calcular_promedio(a, b, c)
print(f'El promedio es {prom}.')