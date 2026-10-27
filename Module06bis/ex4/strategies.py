from abc import ABC, abstractmethod
from ex3.creatures import Creature, TransformCapability


class InvalidStrategyError(Exception):
    """Exceção levantada quando uma estratégia recebe uma entidade incompatível."""
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
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this normal strategy")
        print(creature.attack())


class AggressiveStrategy(BattleStrategy):
    def is_valid(self, creature: Creature) -> bool:
        # A validação ocorre contra a Capability, nunca contra a classe concreta
        return isinstance(creature, TransformCapability)

    def act(self, creature: Creature) -> None:
        if not self.is_valid(creature):
            raise InvalidStrategyError(f"Invalid Creature '{creature.name}' for this aggressive strategy")
        
        # Casting seguro pois a validação is_valid garantiu o tipo
        tc_creature = creature  # type: ignore
        print(tc_creature.transform())
        print(creature.attack())
        print(tc_creature.revert())