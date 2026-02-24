from Source.BASE import *

if __name__ == '__main__':

    BAGAR.auto_craft("copper_pickaxe",equip=True)
    BAGAR.auto_craft("copper_pickaxe", 3)
    BAGAR.bank_deposit_full_inventory()
    BAGAR.auto_craft("copper_axe", equip=True)
    BAGAR.auto_craft("copper_axe", 3)
    BAGAR.auto_craft("copper_dagger", equip=True)
    BAGAR.auto_craft("copper_dagger", 3)
    BAGAR.bank_deposit_full_inventory()

    while BAGAR.get_character()["weaponcrafting_level"] < 5:
        BAGAR.auto_craft("copper_dagger", recycle=True)
        if copper_helmet == 0 and get_bank_item_quantity("copper_helmet") > 0:
            BAGAR.bank_withdraw_item("copper_helmet")
            BAGAR.equip("copper_helmet")
            copper_helmet = 1
        if copper_boots == 0 and get_bank_item_quantity("copper_boots") > 0:
            BAGAR.bank_withdraw_item("copper_boots")
            BAGAR.equip("copper_boots")
            copper_boots = 1
        if wooden_shield == 0 and get_bank_item_quantity("wooden_shield") > 0:
            BAGAR.bank_withdraw_item("wooden_shield")
            BAGAR.equip("wooden_shield")
            wooden_shield = 1

    BAGAR.bank_deposit_full_inventory()
    BAGAR.auto_craft("sticky_sword", equip=True)
    BAGAR.auto_craft("sticky_sword", 3)

    while BAGAR.get_character()["weaponcrafting_level"] < 10:
        BAGAR.auto_craft("sticky_sword", recycle=True)
        if copper_armor == 0 and get_bank_item_quantity("copper_armor") > 0:
            BAGAR.bank_withdraw_item("copper_armor")
            BAGAR.equip("copper_armor")
            copper_armor = 1
        if copper_legs_armor == 0 and get_bank_item_quantity("copper_legs_armor") > 0:
            BAGAR.bank_withdraw_item("copper_legs_armor")
            BAGAR.equip("copper_legs_armor")
            copper_legs_armor = 1
        if water_bow == 0 and get_bank_item_quantity("water_bow") > 0:
            BAGAR.bank_withdraw_item("water_bow")
            water_bow = 1



