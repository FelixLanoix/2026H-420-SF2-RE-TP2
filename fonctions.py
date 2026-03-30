import math

from expression import Expression
from polynome import Polynome
from operations import Multiplication

class Sin(Expression): 
    def __init__(self, u: Expression):
        self.u = u
    
    def evaluer(self, x: float) -> float:
        resultat = math.sin(self.u.evaluer(x))
        return resultat
    
    def deriver(self) -> "Expression":
        resultat = Multiplication(Cos(self.u), self.u.deriver()) # c'est ca pour deriver sin 
        return resultat
    
    def __str__(self) -> str:
        return f"sin({self.u})"

class Cos(Expression):

    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        resultat = math.cos(self.u.evaluer(x))
        return resultat

    def deriver(self) -> "Expression":
        resultat = Multiplication(-1 * Sin(self.u), self.u.deriver())# celui la c'est pour deriver cos
        return resultat

    def __str__(self) -> str:
        return f"cos({self.u})"


class Exp(Expression):
    def __init__(self, u: Expression):
        self.u = u

    def evaluer(self, x: float) -> float:
        resultat = math.exp(self.u.evaluer(x))
        return resultat

    def deriver(self) -> "Expression":
        resultat = Multiplication(Exp(self.u), self.u.deriver())
        return resultat

    def __str__(self) -> str:
        return f"exp({self.u})"

