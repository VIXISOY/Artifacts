from Source.BASE import *

if __name__ == '__main__':

    while True:
        CHOPA.auto_craft("feather_coat")
        CHOPA.bank_withdraw_item("feather_coat")
        CHOPA.recycle("feather_coat")

        if CHOPA.get_character()["level"]  == 5 :

            CHOPA.bank_withdraw_item("feather_coat")
            CHOPA.equip("feather_coat")
            CHOPA.bank_withdraw_item("sticky_sword")
            CHOPA.equip("sticky_sword")
            CHOPA.bank_withdraw_item("copper_legs_armor")
            CHOPA.equip("copper_legs_armor")

    count = 4
    while True:
        CHOPA.auto_craft_self_only("wooden_shield")
        CHOPA.recycle("wooden_shield")

        count += 1

        if count == 5:
            CHOPA.bank_deposit_full_inventory()

    while True:
        CHOPA.bank_deposit_full_inventory()
        if get_bank_item_quantity("spruce_wood") <= 50:
            CHOPA.farm_item("spruce_wood", 50 - get_bank_item_quantity("spruce_wood"))
        CHOPA.bank_deposit_full_inventory()
        CHOPA.bank_withdraw_item("spruce_wood", min(get_bank_item_quantity("spruce_wood"), 50))
        CHOPA.craft("spruce_plank", CHOPA.get_item_quantity("spruce_wood")/10)
