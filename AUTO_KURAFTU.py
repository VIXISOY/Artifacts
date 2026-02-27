from Source.BASE import *

if __name__ == '__main__':

    BAGAR.auto_craft("iron_sword")
    BAGAR.auto_craft("iron_sword")
    BAGAR.auto_craft("iron_sword")

    BAGAR.auto_craft("iron_dagger")
    BAGAR.auto_craft("iron_dagger")
    BAGAR.auto_craft("iron_dagger")

    BAGAR.bank_deposit_full_inventory()

    while True:
        BAGAR.auto_craft("iron_sword", recycle=True)



