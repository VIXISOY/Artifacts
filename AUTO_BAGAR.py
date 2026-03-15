from Source.BASE import *

if __name__ == '__main__':

    while get_bank_item_quantity("fire_and_earth_amulet") < 4:
        BAGAR.auto_craft("fire_and_earth_amulet")


    while True:
         BAGAR.auto_craft("battlestaff",recycle=True)


