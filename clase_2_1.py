# LISTAS Y DICCIONARIOS
# Listas
# Declarar una lista con 8 elementos
lista1 = [1, 2, 3, 4, 5, 6, 7, 8]
print(lista1) # Imprime la lista completa

# Agregamos 2 valores a la lista
lista1.append(9)
lista1.append(10)
print(lista1) # Imprime la lista completa

# Agregamos un valor en una posicion especifica
lista1.insert(3, 20)
print(lista1) # Imprime la lista completa

# Eliminamos un valor de la lista
lista1.remove(20)
print(lista1) # Imprime la lista completa

# Eliminamos un valor de la lista en una posicion especifica
lista1.pop(7)
print(lista1) # Imprime la lista completa

# Eliminamos todos los valores de la lista
lista1.clear()
print(lista1) # Imprime la lista completa

# Eliminamos la lista
# del lista1 # Esto no lo utilicen en sus programas
# print(lista1) # Imprime la lista completa

# Diccionarios
# Declarar un diccionario con 3 elementos con llaves 1,2,3 y valores perro, gato y caballo
diccionario1 = {1: "Perro", 2: "Gato", 3: "Caballo"}
print(diccionario1) # Imprime el diccionario completo

# Agregamos un valor al diccionario
diccionario1[4] = "Aguila"
print(diccionario1) # Imprime el diccionario completo

# Eliminamos un valor del diccionario
del diccionario1[2] # Esto si lo pueden utilizar en sus programas
print(diccionario1) # Imprime el diccionario completo

# Eliminamos todos los valores del diccionario
diccionario1.clear()
print(diccionario1) # Imprime el diccionario completo

# Imprimimos la llave y el valor de cada elemento del diccionario
for llave, valor in diccionario1.items():
    print("La llave es:", llave," y el valor es:", valor)

print('---------------------------------------------')

for keys in diccionario1.keys():
    print("La llave es:", keys, " y el valor es:", diccionario1[keys])


# Declaramos una lista de 5 elementos
lista1 = [1, 2, 3, 4, 5]

# Agregamos una lista a un diccionario
diccionario1[5] = lista1
print(diccionario1) # Imprime el diccionario completo

# Imprimimos el numero 3
print(diccionario1[5][2])

# Diccionario dentro de un diccionario
diccionario2 = {1: "Perro", 2: "Gato", 3: "Caballo", 4: "Aguila", 5: lista1, 6: diccionario1}
print(diccionario2) # Imprime el diccionario completo

