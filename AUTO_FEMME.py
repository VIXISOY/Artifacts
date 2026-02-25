from Source.BASE import *

if __name__ == '__main__':

    while FEMME.get_character()["fishing_level"] < 10:
        FEMME.bank_deposit_full_inventory()
        FEMME.auto_craft("cooked_gudgeon", 50)

    while FEMME.get_character()["fishing_level"] < 20:
        FEMME.bank_deposit_full_inventory()
        FEMME.auto_craft("cooked_shrimp", 50)
