from Source.BASE import *

if __name__ == '__main__':


    while True:
        FEMME.bank_deposit_full_inventory()
        FEMME.auto_craft("cooked_trout",50)
        FEMME.bank_deposit_item("cooked_trout",50)

