from Source.BASE import *

if __name__ == '__main__':

    while True:
        BAGAR.auto_craft("wooden_shield")

    BAGAR.auto_craft("copper_legs_armor")
    BAGAR.bank_withdraw_item("copper_legs_armor")
    BAGAR.equip("copper_legs_armor")

    BAGAR.auto_craft("copper_armor")
    BAGAR.bank_withdraw_item("copper_armor")
    BAGAR.equip("copper_armor")

    BAGAR.auto_craft("feather_coat")
    BAGAR.bank_withdraw_item("copper_ring")
    BAGAR.equip("feather_coat")

    BAGAR.auto_craft("life_amulet")
    BAGAR.bank_withdraw_item("life_amulet")
    BAGAR.equip("life_amulet")
