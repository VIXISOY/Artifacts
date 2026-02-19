from Source.BASE import *

if __name__ == '__main__':

    count = 2
    while True:
        if count == 2:
            CHOPA.bank_deposit_full_inventory()
            count = 0
        count += 1
        CHOPA.auto_craft("hardwood_plank",3)
        CHOPA.auto_craft("spruce_plank",3)


    count = 4
    while True:
        CHOPA.auto_craft_self_only("wooden_shield")
        CHOPA.recycle("wooden_shield")

        count += 1

        if count == 5:
            CHOPA.bank_deposit_full_inventory()
