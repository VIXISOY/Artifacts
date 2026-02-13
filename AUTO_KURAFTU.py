from Source.BASE import *

if __name__ == '__main__':
    BAGAR.bank_deposit_full_inventory()
    while True:
        BAGAR.auto_craft_self_only("life_amulet")
        BAGAR.recycle("life_amulet")
