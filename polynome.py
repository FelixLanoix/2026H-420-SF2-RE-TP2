from expression import Expression


class Polynome(Expression):
    """Polynome represente par une liste de coefficients [a0, a1, a2, ...]."""

    def __init__(self, coefficients: list[float]):
        self.coefficients = coefficients

    def evaluer(self, x: float) -> float:
        resultat = 0 
        for i in range(len(self.coefficients)):
            resultat += self.coefficients[i] * (x ** i)
        return resultat

    def deriver(self) -> "Expression":
        derivee_coefficients = []
        for i in range(1, len(self.coefficients)):
            derivee_coefficients.append(i * self.coefficients[i])
        return Polynome(derivee_coefficients)
    
    def __str__(self) -> str:
        elements = []
        for i in range(len(self.coefficients)):
            if self.coefficients[i] != 0:
                if i == 0:
                    elements.append(f"{self.coefficients[i]}")
                elif i == 1:
                    elements.append(f"{self.coefficients[i]}x")
                else:
                    elements.append(f"{self.coefficients[i]}x^{i}")
        return " + ".join(elements) #permet d'avoir une expression claire du polynome
    
    
