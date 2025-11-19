# EJERCICIO 1 ------------------------------------

#Funcion para calcular el factorial del numero
def fact(numero):
    if numero == 0:
        return 1
    else:
        return numero * fact(numero - 1)
    
for i in range(6): # Para calcular el factorial de 5
    print(f'El factorial de {i} es {fact(i)}')

# EJERCICIO 2 ------------------------------------

#Funcion para calcular fibonacci
def fibonacci_rec(pos):
    if pos == 0:
        return 0
    elif pos == 1:
        return 1
    else:
        return fibonacci_rec(pos - 1) + fibonacci_rec(pos - 2)

posicion = int(input('Ingrese la posicion para conocer el numero de Fibonacci: '))
for i in range(posicion + 1):
    print(f'El número de Fibonacci de la posicion {i} es {fibonacci_rec(i)}')
    

# EJERCICIO 3 ------------------------------------


#Funcion para calcular la potencia de un numero y sumarla
def calcular_potencia(base, exponente):
    if exponente == 0:
        return 1
    elif exponente < 0:
        return 1 / base ** (- exponente)
    else:
        return base * (base ** (exponente - 1))
    
# Algoritmo general de prueba

casos_prueba = [(2,3), (6, 0), (5, 1), (3, 5), (2, -1)]
for base, exp in casos_prueba:
    print(f'La potencia de {base} a la {exp} es: {calcular_potencia(base, exp)}')
    
    
# EJERCICIO 4 ------------------------------------

#Funcion para convertir un numero de decimal a binario
def decimal_a_binario(numero):
    if numero == 0: # Si el numero es cero, devuelve directamente
        return "0"
    
    elif numero == 1: #Si el numero es uno, devuelve directamente
        return "1"
    
    else:
        return decimal_a_binario(numero // 2) + str(numero % 2)

ejemplos_de_uso = [10, 0, 55, 25, 1]
for i in ejemplos_de_uso:
    print(f'La conversión del numero decimal {i} a binario es: {decimal_a_binario(i)}')

# EJERCICIO 5 ------------------------------------

#Funcion para saber si una palabra se considera palindromo
def es_palindromo(palabra):
    if len(palabra) <= 1: # Caso base: Si es 1 letra o vacío es palíndromo
        return True
    
    elif palabra[0] != palabra[-1]: # Si la primer y ultima letra son distintas, no es palindromo
        return False
    
    else:
        return es_palindromo(palabra[1:-1])
    
palabras = ['radar', 'python', 'neuquen', '', 'reconocer']
for i in palabras:
    if es_palindromo(i):
        print(f'La palabra -{i}- es palíndromo.')
    else:
        print(f'La palabra -{i}- no es palíndromo.')

# EJERCICIO 6 ------------------------------------

#Funcion para sumar digitos de un numero
def suma_digitos(num):
    if num < 10: # Si el numero es de un digito, devuelve el mismo numero
        return num
    
    else:
        return num % 10 + suma_digitos(num // 10)
    

numeros = [1234, 10, 55, 103, 565]
for i in numeros:
    print(f'La suma de los dígitos del número {i} es: {suma_digitos(i)}')

# EJERCICIO 7 ------------------------------------

#Funcion para construir piramide con n bloques
def contar_bloques(n):
    if n == 1: # Caso base
        return n
    
    else:
        return n + contar_bloques(n - 1)
    
bloques = [2, 5, 3, 10, 1]
for i in bloques:
    print(f'La piramide con la base de {i} bloque/s necesita {contar_bloques(i)} bloque/s en total.')
    

# EJERCICIO 8 ------------------------------------

#Funcion para contar cuantas veces aparece un digito en un numero
def contar_digito(numero, digito):
    # Caso base: número de un solo dígito
    if numero < 10:
        return 1 if numero == digito else 0
    
    # Obtener último dígito
    ultimo_digito = numero % 10
    
    # Caso recursivo:
    if ultimo_digito == digito:
        return 1 + contar_digito(numero // 10, digito) #Encuentra, suma 1 y vuelve a buscar
    else:
        return contar_digito(numero // 10, digito) #No encuentra, no suma pero vuelve a buscar 
    
prueba = [(12345675520, 5), (111111, 3), (65871238, 8)]
for num, dig in prueba:
    print(f'El dígito <{dig}> aparece {contar_digito(num, dig)} veces en el número <{num}>.')
