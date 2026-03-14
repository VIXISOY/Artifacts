from Source.BASE import *

if __name__ == '__main__':

    while get_bank_item_quantity("hardwood_plank") < 100:
        CHOPA.auto_craft("hardwood_plank",5)

    while CHOPA.get_character()["gearcrafting_level"] < 30:
        CHOPA.auto_craft("hard_leather_boots",recycle=True)

