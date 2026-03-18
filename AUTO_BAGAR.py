from Source.BASE import *

if __name__ == '__main__':

    while True:
         BAGAR.farm_item("tasks_coin")
         BAGAR.bank_deposit_item("tasks_coin", BAGAR.get_item_quantity("tasks_coin"))


