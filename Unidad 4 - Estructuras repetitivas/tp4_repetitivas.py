# Ejercicio 1

for i in range(101):
    print(i)


# Ejercicio 2

numero = int(input('Ingrese un número entero\n'))
numero = abs(numero)
cont = 0

if numero == 0:
    cont = 1
else:
    while numero > 0:
        numero = int(numero/10)
        cont += 1

print('La cantidad de digitos que contiene es ', cont)

# Ejercicio 3

num1 = int(input('Ingrese el primer numero entero\n'))
num2 = int(input('Ingrese el segundo numero entero\n'))

if num1 > num2:
    max = num1
    min = num2
elif num1 < num2:
    max = num2
    min = num1
    
sumatoria = 0
    
for i in range(min + 1, max):
    sumatoria += i
    
print('La suma de todos los numeros intermedios es ', sumatoria)
  
# Ejercicio 4

cant_num = int(input("Cuántos números enteros desea ingresar?\n"))

sumatoria = 0

for i in range(1, cant_num + 1):
    print('Ingrese el numero ', i)
    num = int(input())
    sumatoria += num
    opc = int(input('Si desea conocer el total acumulado presione 0 sino presione 1\n'))
    if opc == 0:
        print('La sumatoria parcial es ', sumatoria)
    elif opc == 1:
        continue
    else:
        print('La opción ingresada no es válida.')
        
print('La sumatoria final es ', sumatoria)
 
# Ejercicio 5

import random

num = random.randint(0, 9)
bandera = 0
cont = 0

while bandera == 0:
    num_usuario = int(input('Ingrese un numero entre 0 y 9\n'))
    cont += 1
    if num_usuario == num:
        print('Acertaste!')
        bandera = 1
    else:
        print('Fallaste. Intenta de nuevo!\n')
print(f'Lo adivinaste en {cont} veces.')

# Ejercicio 6

for i in range(100, 0, -2):
    print(i)
    
# Ejercicio 7

num = int(input('Ingrese un numero entero positivo\n'))
sumatoria = 0

if num > 0:
    for i in range (num+1):
        sumatoria += i
    print('La sumatoria es', sumatoria)
else:
    print('El número ingresado no es válido.')
   
# Ejercicio 8

c_par = 0
c_impar = 0
c_pos = 0
c_neg = 0

for i in range(1, 101):
    print(i, ': Ingrese un número entero')
    num = int(input())
    if num > 0:
        c_pos += 1
    if num < 0:
        c_neg += 1
    if num % 2 == 0:
        c_par += 1
    if num % 2 == 1:
        c_impar += 1

print(f'En la lista hay {c_pos} números positivos.')
print(f'En la lista hay {c_neg} números negativos.')
print(f'En la lista hay {c_par} números pares.')
print(f'En la lista hay {c_impar} números impares.')
 
# Ejercicio 9

from statistics import mean

lista=[]

for i in range(1,6):
    print('Ingrese el numero ', i)
    num = int(input())
    lista.append(num)

media = mean(lista)
print('La media es ', media)

# Ejercicio 10

num_invertido = 0
digito = 0

num = int(input('Ingrese un numero entero positivo\n'))

while num > 0:
    digito = num % 10
    num_invertido = (num_invertido * 10) + digito
    num = num // 10
    
print('El numero invertido es ', num_invertido)
