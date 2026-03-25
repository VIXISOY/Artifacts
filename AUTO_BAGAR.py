from Source.BASE import *

if __name__ == '__main__':

    while BAGAR.get_character()["jewelrycrafting_level"] < 20:
        BAGAR.auto_craft("life_ring",recycle=True)

    while get_bank_item_quantity("ring_of_chance") < 3:
        BAGAR.auto_craft("ring_of_chance")

    while get_bank_item_quantity("skull_wand") < 4:
        BAGAR.auto_craft("skull_wand")

    while get_bank_item_quantity("skull_amulet") < 4:
        BAGAR.auto_craft("skull_amulet")

    while True:
        BAGAR.farm_item("tasks_coin")
        BAGAR.bank_deposit_item("tasks_coin", KRYST.get_item_quantity("tasks_coin"))
        # BAGAR.boss_farm("king_slime", CHOPA,quantity=20)
        # BAGAR.farm_item("tasks_coin")
        # BAGAR.bank_deposit_item("tasks_coin", BAGAR.get_item_quantity("tasks_coin"))


