from abc import ABC, abstractmethod
from ex3.creatures import Creature, TransformCapability


class InvalidStrategyError(Exception):
    """Indica que uma entidade é incompatível com a estratégia."""

    pass


class BattleStrategy(ABC):
    @abstractmethod
    def is_valid(self, creature: Creature) -> bool:
        """Verifica se a criatura atende aos requisitos desta estratégia."""
        pass

    @abstractmethod
    def act(self, creature: Creature) -> None:
        """Executa a rotina de combate."""
        pass


class NormalStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        return isinstance(creature, Creature)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this normal strategy"
            )
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # A validação usa a capability, nunca a classe concreta.
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not isinstance(creature, TransformCapability):
            raise InvalidStrategyError(
                f"Invalid Creature '{creature.name}' "
                "for this aggressive strategy"
            )

        print(creature.transform())
        print(creature.attack())
        print(creature.revert())
