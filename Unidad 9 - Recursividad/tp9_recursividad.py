# EJERCICIO 1 ------------------------------------

#Funcion para calcular el factorial del numero
def fact(numero):
    if numero == 0:
        return 1
    else:
        return numero * fact(numero - 1)
    
#for i in range(6): # Para calcular el factorial de 5
#    print(f'El factorial de {i} es {fact(i)}')

# EJERCICIO 2 ------------------------------------

#Funcion para calcular fibonacci
def fibonacci_rec(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_rec(pos - 1) + fibonacci_rec(pos - 2)

#posicion = int(input('Ingrese la posicion para conocer el numero de Fibonacci: '))
#for i in range(posicion + 1):
#    print(f'El número de Fibonacci de la posicion {i} es {fibonacci_rec(i)}')
    

# EJERCICIO 3 ------------------------------------


#Funcion para calcular la potencia de un numero y sumarla
def calcular_potencia(base, potencia):
    if base == 0:
        return 0
    elif base == 1:
        return 1
    else:
        return base * (base ** (potencia - 1))
    

    
    
# EJERCICIO 4 ------------------------------------
# EJERCICIO 5 ------------------------------------
# EJERCICIO 6 ------------------------------------
# EJERCICIO 7 ------------------------------------
# EJERCICIO 8 ------------------------------------

