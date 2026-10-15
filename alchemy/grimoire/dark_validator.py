"""Dark spell validator demonstrating broken circular import."""

# Import no topo gera dependencia circular com dark_spellbook.py!
from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    """Validates dark ingredients."""
    allowed = dark_spell_allowed_ingredients()
    ing_list = [i.strip().lower() for i in ingredients.split(",")]
    is_valid = any(ing in allowed for ing in ing_list)
    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} {status}"
