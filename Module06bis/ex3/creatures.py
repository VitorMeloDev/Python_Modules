from abc import ABC, abstractmethod


class Creature(ABC):
    """Classe base abstrata para todas as criaturas do sistema."""

    def __init__(self, name: str, element_type: str) -> None:
        self.name = name
        self.element_type = element_type

    @abstractmethod
    def attack(self) -> str:
        """Método abstrato que toda criatura precisa implementar."""
        pass

    def describe(self) -> str:
        """Método concreto que retorna a identificação padrão da criatura."""
        return f"{self.name} is a {self.element_type} type Creature"


# Criaturas Normais (Herdam apenas de Creature)
class Flameling(Creature):
    def __init__(self) -> None:
        super().__init__("Flameling", "Fire")

    def attack(self) -> str:
        return f"{self.name} uses Ember!"


class Pyrodon(Creature):
    def __init__(self) -> None:
        super().__init__("Pyrodon", "Fire/Flying")

    def attack(self) -> str:
        return f"{self.name} uses Flamethrower!"


# Capability/Habilidade Isolada (NÃO herda de Creature!)
class TransformCapability(ABC):
    """Classe abstrata para capacidades de transformação."""

    def __init__(self) -> None:
        self.is_transformed: bool = False

    @abstractmethod
    def transform(self) -> str:
        pass

    @abstractmethod
    def revert(self) -> str:
        pass


# Criaturas com Habilidade de Transformação (Herança Múltipla)
class Shiftling(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Shiftling", "Normal")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} shifts into a sharper form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} returns to normal."

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} performs a boosted strike!"
        return f"{self.name} attacks normally."


class Morphagon(Creature, TransformCapability):
    def __init__(self) -> None:
        Creature.__init__(self, "Morphagon", "Normal/Dragon")
        TransformCapability.__init__(self)

    def transform(self) -> str:
        self.is_transformed = True
        return f"{self.name} morphs into a dragonic battle form!"

    def revert(self) -> str:
        self.is_transformed = False
        return f"{self.name} stabilizes its form."

    def attack(self) -> str:
        if self.is_transformed:
            return f"{self.name} unleashes a devastating morph strike!"
        return f"{self.name} attacks normally."
