from Source.BASE import *
CHOPA = Character("CHOPA")

if __name__ == '__main__':

    while CHOPA.get_character()["gearcrafting_level"] < 35:
        CHOPA.auto_craft("snakeskin_legs_armor",recycle=True)