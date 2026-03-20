from Source.BASE import *

if __name__ == '__main__':

    while get_bank_item_quantity("slime_shield") < 3:
        CHOPA.auto_craft("slime_shield")

    while CHOPA.get_character()["gearcrafting_level"] < 25:
        CHOPA.auto_craft("hard_leather_boots",recycle=True)

    while get_bank_item_quantity("piggy_pants") < 4:
        CHOPA.auto_craft("piggy_pants")

    while get_bank_item_quantity("piggy_armor") < 4:
        CHOPA.auto_craft("piggy_armor")