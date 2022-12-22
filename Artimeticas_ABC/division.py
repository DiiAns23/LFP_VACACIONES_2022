from expression import *

class Division(Expression):

    def __init__(self, n1,n2):
        super().__init__(n1,n2)
    
    def ejecutar(self):
        if(self.n2!=0):
            return self.n1 / self.n2
        else:
            return 0
        