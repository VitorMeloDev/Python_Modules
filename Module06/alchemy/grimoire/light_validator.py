def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    allowed = light_spell_allowed_ingredients()
    ingredients_lower = ingredients.lower()

    is_valid = False
    for i in allowed:
        if i in ingredients_lower:
            is_valid = True
            break

    status = "VALID" if is_valid else "INVALID"
    return f"{ingredients} - {status}"