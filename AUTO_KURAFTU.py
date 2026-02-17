from Source.BASE import *

if __name__ == '__main__':

    #BAGAR.bank_deposit_full_inventory()

    while True:
        BAGAR.auto_craft("iron_dagger",recycle=True)

    count = 0
    while True:
        if count == 50 :
            BAGAR.bank_withdraw_item("cooked_shrimp",50)
            count = 0
        count += 1
        BAGAR.farm_item("wool")
        BAGAR.use("cooked_shrimp",1)


