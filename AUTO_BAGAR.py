from Source.BASE import *

if __name__ == '__main__':

    while BAGAR.get_character()["woodcutting_level"] < 20:
        BAGAR.auto_craft("spruce_plank",5)

    while get_bank_item_quantity("steel_battle_axe") < 4:
        BAGAR.auto_craft("steel_battleaxe")
    # BAGAR.auto_craft("iron_pickaxe")


    # while True:
    #     BAGAR.auto_craft("iron_pickaxe",recycle=True)


