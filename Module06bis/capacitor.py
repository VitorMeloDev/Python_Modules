from ex3 import TransformCreatureFactory
from ex3.creatures import TransformCapability


def exercise_transform(entity_name: str, entity: object) -> None:
    print(f"{entity_name}:")
    if hasattr(entity, "describe"):
        print(entity.describe())
    if hasattr(entity, "attack"):
        print(entity.attack())

    if isinstance(entity, TransformCapability):
        print(entity.transform())
        if hasattr(entity, "attack"):
            print(entity.attack())
        print(entity.revert())


def main() -> None:
    factory = TransformCreatureFactory()
    base = factory.create_base()
    evolved = factory.create_evolved()

    print("Testing Creature with transform capability")
    exercise_transform("base", base)
    exercise_transform("evolved", evolved)


if __name__ == "__main__":
    main()
