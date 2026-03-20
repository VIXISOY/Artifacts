from Source.BASE import *

if __name__ == '__main__':

    while get_bank_item_quantity("piggy_armor") < 3:
        CHOPA.auto_craft("piggy_armor")

    while CHOPA.get_character()["gearcrafting_level"] < 25:
        CHOPA.auto_craft("hard_leather_boots",recycle=True)