from expression import *

class Resta(Expression):

    def __init__(self, n1,n2):
        super().__init__(n1,n2)
    
    def ejecutar(self):
        return self.n1 - self.n2