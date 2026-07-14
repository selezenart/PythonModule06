import alchemy


if __name__ == "__main__":
    print("=== Distillation 1 ===")
    print("Direct access to alchemy/potions.py")
    print("Testing strength_potion: "
          f"{alchemy.strength_potion()}")
    print("Testing heal alias: "
          f"{alchemy.heal()}")
