# Ejemplos de la Clase 2

# LEER INFORMACION DE UN ARCHIVO
# Abrir el archivo
Objeto = open("clase2.ext", "r+") # Abrimos en modo lectura y escritura

# Imprimir la informacion dentro del archivo
print("READ")
print(Objeto.read())

# Cerar el archivo
Objeto.close()

# Volvemos a abrir el archivo
Objeto = open("clase2.ext", "r+")

# Leer un caracter de una linea
print("READLINE")
print(Objeto.readline(-1)) # Pueden cambiarlo por 1, 2, 3, etc

# # Leer una linea
print("READLINE 2")
print(Objeto.readline()) # Lee solo una linea del archivo

# Cerrar el archivo
Objeto.close()


# ESCRIBIR INFORMACION EN UN ARCHIVO
# Abrir el archivo
Objeto = open("clase2.ext", "a") # Abrimos en modo escritura
Objeto.write("\n\tEste texto fue agregado desde Python :3")

# # Cerrar el archivo
Objeto.close()

# Volvemos a abrir el archivo
Objeto = open("clase2.ext", "r+")

# Leer todas las lineas
print("READLINES")
print(Objeto.readlines()) # Aqui se visualiza como una lista
for linea in Objeto.readlines(): # Aqui se visualiza como lineas
    print(linea.strip()) # Elimina los espacios en blanco

# Cerrar el archivo
Objeto.close()

