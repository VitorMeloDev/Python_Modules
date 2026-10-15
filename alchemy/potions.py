"""Potions module demonstrating mixed import paths."""

import elements
from .elements import create_air, create_earth


def healing_potion() -> str:
    """Brews healing potion using internal earth and air elements."""
    return f"Healing potion brewed with '{create_earth()}' and '{create_air()}'"


def strength_potion() -> str:
    """Brews strength potion using root fire and water elements."""
    return (
        f"Strength potion brewed with '{elements.create_fire()}' "
        f"and '{elements.create_water()}'"
    )
