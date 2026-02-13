from Source.BASE import *

if __name__ == '__main__':
    while True:
        FEMME.bank_deposit_full_inventory()
        if get_bank_item_quantity("trout")+FEMME.get_item_quantity("trout") <= 50:
            FEMME.farm_item("trout",50-get_bank_item_quantity("trout")-FEMME.get_item_quantity("trout"))
        FEMME.bank_deposit_full_inventory()
        FEMME.bank_withdraw_item("trout",min(get_bank_item_quantity("trout"),50))
        FEMME.craft("cooked_trout",FEMME.get_item_quantity("trout"))
