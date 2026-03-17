from Source.BASE import *

if __name__ == '__main__':

    # while get_bank_item_quantity("fire_and_earth_amulet") < 4:
    #     BAGAR.auto_craft("fire_and_earth_amulet")


    while True:
         BAGAR.farm_item("tasks_coin")
         BAGAR.bank_deposit_item("tasks_coin", BAGAR.get_item_quantity("tasks_coin"))


