from Source.BASE import *

if __name__ == '__main__':
    BAGAR.auto_craft("copper_armor")
    BAGAR.bank_withdraw_item("copper_armor")
    BAGAR.equip("copper_armor")

    BAGAR.auto_craft("feather_coat")

    while True:
        BAGAR.auto_craft("copper_ring")

    BAGAR.auto_craft("life_amulet")
    BAGAR.bank_withdraw_item("life_amulet")
    BAGAR.equip("life_amulet")
