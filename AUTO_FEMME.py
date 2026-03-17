from Source.BASE import *

if __name__ == '__main__':

    #KRYST.get_character()["fishing_level"] < 20

    while True :
        FEMME.bank_deposit_full_inventory(consumable=True)
        FEMME.auto_craft("cooked_trout",50)
        FEMME.auto_craft("small_health_potion", 30)
