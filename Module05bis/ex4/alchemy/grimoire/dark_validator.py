from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    allowed = dark_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    is_valid = False
    for ingredient in allowed:
        if ingredient in ingredients_lower:
            is_valid = True
            break

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"