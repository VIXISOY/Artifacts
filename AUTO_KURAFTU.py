from Source.BASE import *

if __name__ == '__main__':

    BAGAR.auto_craft("sticky_sword",equip=True)
    BAGAR.recycle("copper_dagger")



    BAGAR.bank_deposit_full_inventory()

    while BAGAR.get_character()["weaponcrafting_level"] < 15:
        BAGAR.auto_craft("sticky_sword", recycle=True)



