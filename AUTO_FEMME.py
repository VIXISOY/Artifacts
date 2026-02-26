from Source.BASE import *

if __name__ == '__main__':

    #KRYST.get_character()["fishing_level"] < 20

    while True :
        FEMME.bank_deposit_full_inventory()
        FEMME.auto_craft("cooked_gudgeon", 50)
        FEMME.bank_deposit_full_inventory()
        FEMME.auto_craft("cooked_shrimp", 50)
        FEMME.bank_deposit_full_inventory()
        FEMME.auto_craft("cooked_gudgeon", 50)
