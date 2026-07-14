# since relative import cant go beyond top lvl package we import
from ..elements import create_air as air
from ..potions import strength_potion as strength
# absolute import
from elements import create_fire as fire


def lead_to_gold():
    return ("Recipe transmuting Lead to "
            f"Gold: brew ’{air()}’ and ’{strength()}’ mixed with ’{fire()}’")
