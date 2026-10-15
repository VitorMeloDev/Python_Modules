"""Transmutation recipes combining absolute and relative imports."""

import elements
from alchemy.elements import create_air
from ..potions import strength_potion


def lead_to_gold() -> str:
    """Transmutes lead to gold combining air, strength potion, and fire."""
    air = create_air()
    strength = strength_potion()
    fire = elements.create_fire()
    return (
        f"Recipe transmuting Lead to Gold: brew '{air}' and '{strength}' "
        f"mixed with '{fire}'"
    )
