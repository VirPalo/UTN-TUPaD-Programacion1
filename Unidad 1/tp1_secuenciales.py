# Ejercicio 1

print("Hola Mundo!")

# Ejercicio 2

nombre = input("Como es tu nombre?\n")
print(f"Hola {nombre}, bienvenido/a!")

# Ejercicio 3

nombre = input("Por favor, ingrese su nombre.\n")
apellido = input("Por favor, ingrese su apellido.\n")
edad = int(input("Por favor, ingrese su edad.\n"))
lugar = input("Por favor, ingrese su lugar de residencia.\n")

print(f"Soy {nombre} {apellido}, tengo {edad} años, y vivo en {lugar}.")

# Ejercicio 4

radio = float(input("Ingrese el radio de un circulo\n"))
area = 3.14159 * pow(radio, 2)
perimetro = 2 * 3.14159 * radio
print(f"El perimetro del circulo es {perimetro} y el area del circulo es {area}")

# Ejercicio 5

seg = int(input("Ingrese una cantidad de segundos para conocer su equivalente en horas.\n"))
horas = (seg / 60) / 60
print(f"Equivale a {horas} horas.")

# Ejercicio 6

num = int(input("Ingrese un numero entero.\n"))
for i in range(11):
    mult = num * i
    print(f"{num} x {i} = {mult}")
    
# Ejercicio 7

num1 = int(input('Ingrese el primer numero entero distinto de 0\n'))
num2 = int(input('Ingrese el segundo numero entero distinto de 0\n'))

suma = num1 + num2
print(f"{num1} + {num2} = {suma}")

resta = num1 - num2
print(f"{num1} - {num2} = {resta}")

multi = num1 * num2
print(f"{num1} * {num2} = {multi}")

division = num1 / num2
print(f"{num1} / {num2} = {division}")

# Ejercicio 8

peso = float(input("Ingrese su peso [kg]\n"))
altura = float(input("Ingrese su altura [m]\n"))

print("Su Indice de Masa Corporal es", peso / altura)

# Ejercicio 9

tempC = float(input("Ingrese la temperatura en grados Celsius\n"))

tempF = ((9/5) * tempC) + 32
print("La temperatura en grados Farenheit es", tempF)

# Ejercicio 10

num1 = int(input('Ingrese el primer numero entero\n'))
num2 = int(input('Ingrese el segundo numero entero\n'))
num3 = int(input('Ingrese el tercer numero entero\n'))

prom = (num1 + num2 + num3) / 3

print("El promedio de los numeros ingresados es", prom)