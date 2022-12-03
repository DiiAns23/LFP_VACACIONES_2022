# Esto nos sirver para realizar comentarios

# Para imprimir en pantalla usamos la función print
print("Hola mundo")

# Para declarar variables usamos el signo =
variable_1 = 10

print("Valor de la variable 1: ", variable_1)

variable_1 = "Hola"

print("Valor de la variable 1: ", variable_1)

variable_1 = 3*variable_1

print("Valor de la variable 1: ", variable_1)

variable_1 = 3.1416

print("Valor de la variable 1: ", variable_1)

variable_1 = True

print("Valor de la variable 1: ", variable_1)

# variable_1 que sea una lista
variable_1 = [1, 2, 3, 4, 5]

print("Valor de la variable 1: ", variable_1)

# variable_1 que sea una tupla
variable_1 = (1, 2, 3, 4, 5)

print("Valor de la variable 1: ", variable_1)

variable_2 = True
variable_3 = 15
# Condicionales
# if
if (variable_2):
    print("La variable es verdadera")

# if - else
if not variable_2:
    print("La variable es falsa")
else:
    print("La variable es verdadera")


# if - elif - else
if variable_3 > 15:
    print("La variable es mayor a 15")
elif variable_3 > 20:
    print("La variable es menor a 15")
elif variable_3 == 15:
    print("La variable es igual a 15")


# Ciclos
# for
variable_4 = [5,4,3,2,1]
for i in range(10):
    print(i)

for i in variable_4:
    print(i)

for i in range(len(variable_4)):
    print(variable_4[i])

# while
i = 0
while i < 10:
    print("El valor de i es: ", i)
    i += 1


# Diccionarios
estudiantes = { 1: "Alan Misael", 2: "Alejandro Jose", 3: "Alejandro Rene" }
print(estudiantes[2])

for i in estudiantes:
    print(estudiantes[i])
else:
    print("Fin del ciclo")

# Funciones
# Primero la definimos con "def", luego el nombre de la función y los parámetros

def suma(a:int, b:int) -> int:
    return a+b

def resta(a,b):
    return a-b

def multiplicacion(a,b):
    return a*b

def division(a,b):
    return a/b  # Siempre nos va a devolver un float
    # int / int = float
    # int / float = float
    # float / int = float
    # float / float = float

# Llamamos a la función
a = suma(3,4)
b = resta(7,3)
c = multiplicacion(2,3)
d = division(10,2)

print("La suma es: ", a)
print("La resta es: ", b)
print("La multiplicacion es: ", c)
print("La division es: ", d)
