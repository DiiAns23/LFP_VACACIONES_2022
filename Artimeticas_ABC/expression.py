from abc import ABC, abstractmethod

class Expression(ABC):

    def __init__(self, n1, n2):
        self.n1 = n1
        self.n2 = n2
    
    @abstractmethod
    def ejecutar(self):
        pass