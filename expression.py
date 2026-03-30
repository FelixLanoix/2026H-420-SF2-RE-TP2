from abc import ABC, abstractmethod


class Expression(ABC):

    @abstractmethod
    def evaluer(self, x: float) -> float:
        pass

    @abstractmethod
    def deriver(self) -> "Expression":
        pass

    @abstractmethod
    def __str__(self) -> str:
        pass
