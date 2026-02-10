from BASE import *

if __name__ == '__main__':
    while True:
        FEMME.bank_deposit_full_inventory()
        if get_bank_item_quantity("gudgeon") <= 50:
            FEMME.farm_item("gudgeon",50-get_bank_item_quantity("gudgeon"))
        FEMME.bank_deposit_full_inventory()
        FEMME.bank_withdraw_item("gudgeon",min(get_bank_item_quantity("gudgeon"),50))
        FEMME.craft("cooked_gudgeon",FEMME.get_item_quantity("gudgeon"))
