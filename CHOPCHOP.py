from Source.BASE import *

if __name__ == '__main__':

    while CHOPA.get_character()["gearcrafting_level"] < 20:
        CHOPA.farm_item("red_slimeball")

    CHOPA.auto_craft("adventurer_vest",equip=True)
    CHOPA.auto_craft("adventurer_vest")
    CHOPA.auto_craft("adventurer_vest")
    CHOPA.auto_craft("adventurer_vest")

    while CHOPA.get_character()["gearcrafting_level"] < 20:
        CHOPA.auto_craft("adventurer_vest", recycle=True)
        CHOPA.bank_deposit_full_inventory()

