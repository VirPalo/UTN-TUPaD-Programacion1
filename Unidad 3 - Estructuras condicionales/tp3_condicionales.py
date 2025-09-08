# Ejercicio 1

edad = int(input('Por favor, ingrese su edad\n'))

if edad >= 18:
    print('Es mayor de edad')

# Ejercicio 2

nota = float(input('Por favor, ingrese su nota\n'))

if nota >= 6:
    print('Aprobado')
else:
    print('Desaprobado')

# Ejercicio 3

num = int(input('Por favor, ingrese un número\n'))

if num % 2 == 0:
    print('Ha ingresado un número par')
else:
    num = int(input('Por favor, ingrese un número par\n'))

# Ejercicio 4

edad = int(input('Por favor, ingrese su edad\n'))

if edad <= 12 and edad>=0:
    print('Niño/a')
elif edad >= 12 and edad < 18:
    print('Adolescente')
elif edad >= 18 and edad < 30:
    print('Adulto/a joven')
elif edad >= 30:
    print('Adulto/a')
else:
    print('El número ingresado no es válido.')


# Ejercicio 5

contrasenia = input('Ingrese una contraseña que tenga entre 8 y 14 caracteres\n')

if len(contrasenia) >= 8 and len(contrasenia) <= 14:
    print('Ha ingresado una contraseña correcta')
else:
    print('Por favor, ingrese una contraseña de entre 8 y 14 caracteres') 

# Ejercicio 6

import random
from statistics import mode, median, mean

num_aleat = [random.randint(1,100) for i in range(50)]

mod = mode(num_aleat)
med = median(num_aleat)
mea = mean(num_aleat)

print(f'El valor de la moda es {mod}, el valor de la mediana es {med} y el valor de la media es {mea}')

if mea > med and med > mod:
    print('Se tiene un sesgo positivo o a la derecha')
elif mea < med and med < mod:
    print('Se tiene un sesgo negativo o a la izquierda')
elif mea == med and med == mod:
    print('Sin sesgo, ya que la media, la moda y la mediana son iguales')

# Ejercicio 7

frase = input('Ingrese una palabra o frase por pantalla\n')

if frase[-1] == 'a' or frase[-1] == 'e' or frase[-1] == 'i' or frase[-1] == 'o' or frase[-1] == 'u':
    frase = frase + '!'
    print(frase)
else:
    print(frase)

# Ejercicio 8

nombre = input('Por favor, ingrese su nombre\n')

print('Elija una tarea seleccionando 1, 2 o 3:')
print('1- Si quiere su nombre en mayúsculas. Por ejemplo: PEDRO')
print('2- Si quiere su nombre en minusculas. Por ejemplo: pedro')
print('3- Si quiere su nombre con la primer letra mayúscula. Por ejemplo: Pedro')
opc = int(input('Ingrese la opción elegida\n'))

if opc == 1:
    nombre = nombre.upper()
    print(nombre)
elif opc == 2:
    nombre = nombre.lower()
    print(nombre)
elif opc == 3:
    nombre = nombre.title()
    print(nombre)
else:
    print('La opción ingresada no es válida.')

# Ejercicio 9

magnitud = int(input('Por favor, ingrese la magnitud del terremoto\n'))

if magnitud < 3 and magnitud > 0:
    print('Muy leve')
elif magnitud >= 3 and magnitud < 4:
    print('Leve')
elif magnitud >= 4 and magnitud < 5:
    print('Moderado')
elif magnitud >= 5 and magnitud < 6:
    print('Fuerte')
elif magnitud >= 6 and magnitud < 7:
    print('Muy fuerte')
elif magnitud >= 7:
    print('Extremo')
else:
    print('El valor ingresado no es válido')

# Ejercicio 10

hemisferio = input('Ingrese N si se encuentra en el hemisferio Norte y S si se encuentra en el hemisferio Sur\n')
    
mes = int(input('Por favor, ingrese el mes con número. (1 al 12)\n'))
    
dia = int(input('Finalmente, ingrese el día. (1 al 31)\n'))

if hemisferio == 'N' or hemisferio == 'n':
    if mes == 12:
        if dia >= 21 and dia <= 31:
            print('La estación es Invierno')
        elif dia >= 1 and dia < 21:
            print('La estación es Otoño')
        else:
            print('El día ingresado no es válido')
            
    elif mes == 1 or mes == 2:
        print('La estación es Invierno')
        
    elif mes == 3:
        if dia >= 1 and dia <= 20:
            print('La estación es Invierno')
        elif dia > 20 and dia <= 31:
            print('La estación es Primavera')
        else:
            print('El día ingresado no es válido')
            
    elif mes == 4 or mes == 5:
        print('La estación es Primavera')
    
    elif mes == 6:
        if dia >= 1 and dia <= 20:
            print('La estación es Primavera')
        elif dia > 20 and dia <= 30:
            print('La estación es Verano')
        else:
            print('El día ingresado no es válido')
        
    elif mes == 7 or mes == 8:
        print('La estación es Verano')
    
    elif mes == 9:
        if dia >= 1 and dia <= 20:
            print('La estación es Verano')
        elif dia > 20 and dia <= 30:
            print('La estación es Otoño')
        else:
            print('El día ingresado no es válido')
    
    elif mes == 10 or mes == 11:
        print('La estación es Otoño')
    
    else:
        print('El mes ingresado no es válido')
        
elif hemisferio == 'S' or hemisferio == 's':
    if mes == 12:
        if dia >= 21 and dia <= 31:
            print('La estación es Verano')
        elif dia >= 1 and dia < 21:
            print('La estación es Primavera')
        else:
            print('El día ingresado no es válido')
            
    elif mes == 1 or mes == 2:
        print('La estación es Verano')
        
    elif mes == 3:
        if dia >= 1 and dia <= 20:
            print('La estación es Verano')
        elif dia > 20 and dia <= 31:
            print('La estación es Otoño')
        else:
            print('El día ingresado no es válido')
            
    elif mes == 4 or mes == 5:
        print('La estación es Otoño')
    
    elif mes == 6:
        if dia >= 1 and dia <= 20:
            print('La estación es Otoño')
        elif dia > 20 and dia <= 30:
            print('La estación es Invierno')
        else:
            print('El día ingresado no es válido')
        
    elif mes == 7 or mes == 8:
        print('La estación es Invierno')
    
    elif mes == 9:
        if dia >= 1 and dia <= 20:
            print('La estación es Invierno')
        elif dia > 20 and dia <= 30:
            print('La estación es Primavera')
        else:
            print('El día ingresado no es válido')
    
    elif mes == 10 or mes == 11:
        print('La estación es Primavera')
    
    else:
        print('El mes ingresado no es válido')
    
else:
    print('El hemisferio ingresado no es válido')
