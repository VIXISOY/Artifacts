from Source.BASE import *

if __name__ == '__main__':


    while BAGAR.get_character()["jewelrycrafting_level"] < 5:
        BAGAR.auto_craft("copper_ring",recycle=True)

    while BAGAR.get_character()["jewelrycrafting_level"] < 10:
        BAGAR.auto_craft("life_amulet",recycle=True)

    while get_bank_item_quantity("iron_ring") < 8:
        BAGAR.auto_craft("iron_ring")

    while True:
        BAGAR.auto_craft("iron_ring",recycle=True)


