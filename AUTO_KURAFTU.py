from Source.BASE import *

if __name__ == '__main__':

    while BAGAR.get_character()["woodcutting_level"] < 10:
        BAGAR.auto_craft("ash_plank")

    while get_bank_item_quantity("iron_pickaxe") < 4:
        BAGAR.auto_craft("iron_pickaxe")

    while True:
        BAGAR.auto_craft("iron_pickaxe",recycle=True)


