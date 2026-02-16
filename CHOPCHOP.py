from Source.BASE import *

if __name__ == '__main__':

    CHOPA.auto_craft("iron_shield")
    CHOPA.withdraw("iron_shield")
    CHOPA.equip("iron_shield")
    while True:
        sleep(1)

    CHOPA.auto_craft("spruce_plank",4)
    while True:
        CHOPA.auto_craft("hardwood_plank")


    count = 4
    while True:
        CHOPA.auto_craft_self_only("wooden_shield")
        CHOPA.recycle("wooden_shield")

        count += 1

        if count == 5:
            CHOPA.bank_deposit_full_inventory()
