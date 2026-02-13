from Source.BASE import *

if __name__ == '__main__':
    #KRYST.fighting_smart = True
    #for i in range(10):
    
    while True:
        if get_bank_item_quantity("algae") > 20:
            KRYST.auto_craft("minor_health_potion",20)
            KRYST.bank_deposit_full_inventory()
        else:
            KRYST.farm_item("nettle_leaf",80)
            KRYST.bank_deposit_full_inventory()