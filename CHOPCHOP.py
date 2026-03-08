from Source.BASE import *

if __name__ == '__main__':

    #while CHOPA.get_character()["gearcrafting_level"] < 20:
    #    CHOPA.farm_item("red_slimeball")
    while get_bank_item_quantity("adventurer_boots") < 4:
        CHOPA.auto_craft("adventurer_boots")

    while get_bank_item_quantity("adventurer_pants") < 4:
        CHOPA.auto_craft("adventurer_pants")


    while CHOPA.get_character()["gearcrafting_level"] < 25:
        CHOPA.auto_craft("adventurer_boots",recycle=True)

