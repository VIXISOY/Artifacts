from Source.BASE import *

if __name__ == '__main__':

    BAGAR.auto_craft("iron_axe")

    while get_bank_item_quantity("skull_staff") < 4:
        BAGAR.auto_craft("skull_staff")

    while get_bank_item_quantity("battlestaff") < 4:
        BAGAR.auto_craft("battlestaff")
    # BAGAR.auto_craft("iron_pickaxe")


    # while True:
    #     BAGAR.auto_craft("iron_pickaxe",recycle=True)


