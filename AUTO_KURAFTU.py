from Source.BASE import *

if __name__ == '__main__':

    while get_bank_item_quantity("life_amulet") < 5:
        BAGAR.auto_craft("life_amulet")

    while True:
        BAGAR.auto_craft("iron_ring",recycle=True)


