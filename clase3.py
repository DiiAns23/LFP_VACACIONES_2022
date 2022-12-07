# EJEMPLO DE FUNCIONES Y CLASES

# clase de Funciones aritmeticas
class FuncionesAritmeticas:

    def __init__(self, a, b):
        self.a = a
        self.b = b

    # Funcion suma
    def suma(self):
        return self.a + self.b

    # Funcion resta
    def resta(self):
        return self.a - self.b

    # Funcion multiplicacion
    def multiplicacion(self):
        return self.a * self.b

    # Funcion division
    def division(self):
        # revisar que b no sea nulo
        if self.b == 0:
            return 'No se puede dividir entre 0'
        else:
            return self.a / self.b
    
    # Funcion potencia
    def potencia(self,a,b):
        return a**b
    
    def multiparametros(self, *args):
        # imprimir los argumentos
        print(args)
        # devolver la suma de todos los argumentos
        suma = 0
        for i in args:
            suma += i
        return suma

# Declaramos una variable de tipo FuncionesAritmeticas
variable_1 = FuncionesAritmeticas(10, 5)

# Imprimimos los resultados
print('La suma es: ', variable_1.suma())
print('La resta es: ', variable_1.resta())
print('La multiplicacion es: ', variable_1.multiplicacion())
print('La division es: ', variable_1.division())
print('La potencia es: ', variable_1.potencia(2,3))
print('La suma de los multiparametros es: ', variable_1.multiparametros(1,2,3,4,5,6,7,8,9,10))