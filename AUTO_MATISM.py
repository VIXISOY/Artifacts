from Source.BASE import *

if __name__ == '__main__':
    while CHILD.get_character()["weaponcrafting_level"] < 5:
      CHILD.auto_craft("copper_dagger")
      CHILD.bank_deposit_item("copper_dagger",CHILD.get_item_quantity("copper_dagger"))
    CHILD.auto_craft("water_bow")
    