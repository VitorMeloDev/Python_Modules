"""Light spellbook using local import to avoid circular dependency."""

def light_spell_allowed_ingredients() -> list[str]:
    """Returns list of ingredients allowed for light spells."""
    return ["earth", "air", "fire", "water"]


def light_spell_record(spell_name: str, ingredients: str) -> str:
    """Records a light spell after validating ingredients."""
    # Lazy Import: Importado aqui dentro evita dependencia circular no carregamento
    from .light_validator import validate_ingredients

    validation_result = validate_ingredients(ingredients)
    return f"Spell recorded: {spell_name} ({validation_result})"
