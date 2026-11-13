from abc import ABC, abstractmethod
from ex3.creatures import (
    Creature,
    Flameling,
    Pyrodon,
    Shiftling,
    Morphagon,
)


class CreatureFactory(ABC):
    """Interface abstrata da fábrica de criaturas."""

    @abstractmethod
    def create_base(self) -> Creature:
        pass

    @abstractmethod
    def create_evolved(self) -> Creature:
        pass


class FlameFactory(CreatureFactory):
    """Fábrica para a família de fogo (Flameling / Pyrodon)."""

    def create_base(self) -> Creature:
        return Flameling()

    def create_evolved(self) -> Creature:
        return Pyrodon()


class TransformCreatureFactory(CreatureFactory):
    """Fábrica para Shiftling e Morphagon, com capacidade de transformação."""

    def create_base(self) -> Creature:
        return Shiftling()

    def create_evolved(self) -> Creature:
        return Morphagon()
