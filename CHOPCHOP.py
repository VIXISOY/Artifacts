from Source.BASE import *

if __name__ == '__main__':
    while True:
        CHOPA.auto_craft_self_only("wooden_shield")
        CHOPA.recycle("wooden_shield")
    while True:
        CHOPA.bank_deposit_full_inventory()
        if get_bank_item_quantity("spruce_wood") <= 50:
            CHOPA.farm_item("spruce_wood", 50 - get_bank_item_quantity("spruce_wood"))
        CHOPA.bank_deposit_full_inventory()
        CHOPA.bank_withdraw_item("spruce_wood", min(get_bank_item_quantity("spruce_wood"), 50))
        CHOPA.craft("spruce_plank", CHOPA.get_item_quantity("spruce_wood")/10)
