from Source.BASE import *

if __name__ == '__main__':
    while True:
        CHOPA.bank_deposit_full_inventory()
        if get_bank_item_quantity("ash_wood") <= 50:
            CHOPA.farm_item("ash_wood", 50 - get_bank_item_quantity("ash_wood"))
        CHOPA.bank_deposit_full_inventory()
        CHOPA.bank_withdraw_item("ash_wood", min(get_bank_item_quantity("ash_wood"), 50))
        CHOPA.craft("ash_plank", CHOPA.get_item_quantity("ash_wood")/10)
