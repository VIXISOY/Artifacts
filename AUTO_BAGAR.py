from Source.BASE import *
BAGAR = Character("BAGAR")


if __name__ == '__main__':

    while True:
        BAGAR.farm_item("tasks_coin")
        BAGAR.bank_deposit_item("tasks_coin", BAGAR.get_item_quantity("tasks_coin"))
        # BAGAR.boss_farm("king_slime", CHOPA,quantity=20)
        # BAGAR.farm_item("tasks_coin")
        # BAGAR.bank_deposit_item("tasks_coin", BAGAR.get_item_quantity("tasks_coin"))


