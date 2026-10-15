"""Light spell validator."""

from .light_spellbook import light_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validates if given ingredients contain at least one allowed ingredient."""
    allowed = light_spell_allowed_ingredients()
    ing_list = [i.strip().lower() for i in ingredients.split(",")]
    is_valid = any(ing in allowed for ing in ing_list)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} {status}"
