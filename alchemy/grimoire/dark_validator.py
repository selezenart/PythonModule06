from .dark_spellbook import dark_spell_allowed_ingredients


def validate_ingredients(ingredients: str) -> str:
    ingr_list = dark_spell_allowed_ingredients()
    if any(ingr in ingredients for ingr in ingr_list):
        return (f"{ingredients} - VALID")
    return (f"{ingredients} - INVALID")
