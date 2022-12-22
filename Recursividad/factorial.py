# 5! = 5x4x3x2x1 = 120

# Metodo 1 sin recursividad
def factorial(n):

    if n == 0:
        return 1

    for i in range(1, n):
        n = n * i

    return n

# Metodo 2 con recursividad
def factorial_r(n):
    # Detener el ciclo
    if n == 0:
        return 1
    # La manipulacion de los datos
    else:
        return n * factorial_r(n-1)
    # Llamada recursiva o llamada a si mismo

print(factorial_r(6))