from Source.BASE import *

if __name__ == '__main__':

    BAGAR.move_to("mithril_rocks")

    BAGAR.move_to("gold_rocks")

    BAGAR.move_to("chicken")

    while get_bank_item_quantity("steel_axe") < 1:
        BAGAR.auto_craft("steel_axe")

    while get_bank_item_quantity("steel_pickaxe") < 2:
        BAGAR.auto_craft("steel_pickaxe")

    while get_bank_item_quantity("steel_fishing_rod") < 1:
        BAGAR.auto_craft("steel_fishing_rod")

    while get_bank_item_quantity("steel_gloves") < 1:
        BAGAR.auto_craft("steel_gloves")

    while get_bank_item_quantity("chance_ring") < 3:
        BAGAR.auto_craft("chance_ring")

    while get_bank_item_quantity("skull_wand") < 4:
        BAGAR.auto_craft("skull_wand")

    while get_bank_item_quantity("skull_amulet") < 4:
        BAGAR.auto_craft("skull_amulet")

    while True:
        KRYST.farm_item("tasks_coin")
        KRYST.bank_deposit_item("tasks_coin", KRYST.get_item_quantity("tasks_coin"))
        # BAGAR.boss_farm("king_slime", CHOPA,quantity=20)
        # BAGAR.farm_item("tasks_coin")
        # BAGAR.bank_deposit_item("tasks_coin", BAGAR.get_item_quantity("tasks_coin"))


