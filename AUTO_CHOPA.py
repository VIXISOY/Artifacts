from Source.BASE import *

if __name__ == '__main__':

    while CHOPA.get_character()["gearcrafting_level"] < 25:
        CHOPA.auto_craft("hard_leather_boots",recycle=True)