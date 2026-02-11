from Source.BASE import *

if __name__ == '__main__':
    while CHILD.get_character()["gearcrafting_level"] < 5:
      CHILD.auto_craft("copper_helmet")
    CHILD.auto_craft("feather_coat")
    CHILD.auto_craft("copper_legs_armor")
    while CHILD.get_character()["weaponcrafting_level"] < 5:
      CHILD.auto_craft("copper_dagger")
    CHILD.auto_craft("water_bow")
    