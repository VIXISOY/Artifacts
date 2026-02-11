from Source.BASE import *

if __name__ == '__main__':
    while True:
        FEMME.bank_deposit_full_inventory()
        if get_bank_item_quantity("shrimp") <= 50:
            FEMME.farm_item("shrimp",50-get_bank_item_quantity("shrimp"))
        FEMME.bank_deposit_full_inventory()
        FEMME.bank_withdraw_item("shrimp",min(get_bank_item_quantity("shrimp"),50))
        FEMME.craft("cooked_shrimp",FEMME.get_item_quantity("shrimp"))
