def validate_ingredients(ingredients: str) -> str:
    from .light_spellbook import light_spell_allowed_ingredients
    ingr_list = light_spell_allowed_ingredients()
    if any(ingr in ingredients for ingr in ingr_list):
        return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
