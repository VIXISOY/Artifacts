from Source.BASE import *

if __name__ == '__main__':
    #KRYST.fighting_smart = True
    #for i in range(10):
    
    while KRYST.get_character()["woodcutting_level"] < 10:
        KRYST.farm_item("ash_wood",60)
        KRYST.auto_craft("ash_plank",4)
        KRYST.bank_deposit_full_inventory()
    while True:
        KRYST.farm_item("spruce_wood",60)
        KRYST.auto_craft("spruce_plank",6)
        KRYST.bank_deposit_full_inventory()


        
