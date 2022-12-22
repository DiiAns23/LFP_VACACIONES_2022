class Producciones:
    def __init__(self, origen, destinos):
        self.origen = origen
        self.destinos = destinos

class Gramatica:

    def __init__(self, nombre, no_terminales, terminales, nti, producciones):
        self.nombre = nombre
        self.no_terminales = no_terminales
        self.terminales = terminales
        self.nti = nti
        self.producciones = producciones