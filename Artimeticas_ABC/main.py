from suma import Suma
from resta import Resta
from multiplicacion import Multiplicacion
from division import Division

objeto = open("operaciones.txt","r")
#leer lineas
lineas = objeto.readlines()
#recorrer lineas
lista_operaciones = []
for linea in lineas:
    n1 = int(linea[0])
    op = str(linea[1])
    n2 = int(linea[2])
    if(op == "+"):
        lista_operaciones.append(Suma(n1,n2))
    elif(op == "-"):
        lista_operaciones.append(Resta(n1,n2))
    elif(op == "*"):
        lista_operaciones.append(Multiplicacion(n1,n2))
    elif(op == "/"):
        lista_operaciones.append(Division(n1,n2))

for operacion in lista_operaciones:
    print(operacion.ejecutar())

