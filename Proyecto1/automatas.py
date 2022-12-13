class Automata:
    def __init__(self, nombre, estados, alfabeto, estado_inicial, estados_aceptacion, transiciones):
        self.nombre = nombre
        self.estados = estados
        self.alfabeto = alfabeto
        self.estado_inicial = estado_inicial
        self.estados_aceptacion = estados_aceptacion
        self.transiciones = transiciones # origen, valor y destino
    
    def __str__(self):
        return f"Nombre: {self.nombre}\nEstados: {self.estados}\nAlfabeto: {self.alfabeto}\nEstado inicial: {self.estado_inicial}\nEstados de aceptacion: {self.estados_aceptacion}\nTransiciones: {self.transiciones.__str__()}"
    

class Transicion:
    def __init__(self, origen, entrada, destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino
    
    def __str__(self):
        return f"({self.origen}, {self.entrada}; {self.destino})"