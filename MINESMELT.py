from BASE import *

if __name__ == '__main__':
    while True:
        quantity = 80
        CHILD.bank_deposit_full_inventory()
        if get_bank_item_quantity("copper_ore") <= quantity:
            CHILD.farm_item("copper_ore",quantity)
        CHILD.bank_deposit_full_inventory()
        CHILD.bank_withdraw_item("copper_ore",min(get_bank_item_quantity("copper_ore")))
        CHILD.craft("copper_bar",int(CHILD.get_item_quantity("copper_ore")/10))
