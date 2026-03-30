from expression import Expression


class Addition(Expression):
    def __init__(self, u: Expression, v: Expression): #u est le terme a gauche et v celui a droit donc u + v
        self.u = u
        self.v = v

    def evaluer(self, x: float) -> float:
        resultat = self.u.evaluer(x) + self.v.evaluer(x)
        return resultat

    def deriver(self) -> "Expression":
        resultat = Addition(self.u.deriver(), self.v.deriver())
        return resultat

    def __str__(self) -> str:
        resultat = f"({self.u} + {self.v})"
        return resultat


class Multiplication(Expression):
    def __init__(self, u: Expression, v: Expression): 
        self.u = u
        self.v = v

    def evaluer(self, x: float) -> float:
        resultat = self.u.evaluer(x) * self.v.evaluer(x)
        return resultat

    def deriver(self) -> "Expression":
        resultat = Addition(Multiplication(self.u.deriver(), self.v), Multiplication(self.u, self.v.deriver()))
        return resultat

    def __str__(self) -> str:
        resultat = f"({self.u} * {self.v})"
        return resultat
