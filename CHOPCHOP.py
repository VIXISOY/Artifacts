from Source.BASE import *

if __name__ == '__main__':

    #while CHOPA.get_character()["gearcrafting_level"] < 20:
    #    CHOPA.farm_item("red_slimeball")

    while CHOPA.get_character()["gearcrafting_level"] < 25:
        CHOPA.auto_craft("adventurer_pants",recycle=True)

