"""Dark spellbook demonstrating broken circular import (NAIVE WAY)."""

# Import no topo gera dependencia circular com dark_validator.py!
from .dark_validator import validate_ingredients


def dark_spell_allowed_ingredients() -> list[str]:
    """Returns list of ingredients allowed for dark spells."""
    return ["bats", "frogs", "arsenic", "eyeball"]


def dark_spell_record(spell_name: str, ingredients: str) -> str:
    """Attempts to record a dark spell."""
    validation_result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation_result})"
