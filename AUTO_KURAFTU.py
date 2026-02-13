from Source.BASE import *

if __name__ == '__main__':
    BAGAR.bank_deposit_full_inventory()
    count = 4
    while True:
        BAGAR.auto_craft_self_only("life_amulet")
        BAGAR.recycle("life_amulet")

        count += 1

        if count == 5:
            BAGAR.bank_deposit_full_inventory()
            count = 0
