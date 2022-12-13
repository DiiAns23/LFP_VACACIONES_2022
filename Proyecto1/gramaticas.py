class Gramatica:
    def __init__(self, nombre, no_terminales, terminales, no_terminal_inicial, producciones):
        self.nombre = nombre
        self.no_terminales = no_terminales
        self.terminales = terminales
        self.no_terminal_inicial = no_terminal_inicial
        self.producciones = producciones

class Produccion:
    def __init__(self, origen, entrada, destino):
        self.origen = origen
        self.entrada = entrada
        self.destino = destino

    def __str__(self):
        return f"({self.origen}, {self.entrada}; {self.destino})"