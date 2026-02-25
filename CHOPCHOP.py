from Source.BASE import *

if __name__ == '__main__':

    CHOPA.auto_craft("wooden_shield", equip=True)
    CHOPA.auto_craft("wooden_shield")
    CHOPA.auto_craft("wooden_shield")
    CHOPA.auto_craft("wooden_shield")
    CHOPA.bank_deposit_full_inventory()

    while CHOPA.get_character()["gearcrafting_level"] < 5:
        CHOPA.auto_craft("wooden_shield", recycle=True)
        if copper_helmet == 0 and get_bank_item_quantity("copper_helmet") > 0:
            CHOPA.bank_withdraw_item("copper_helmet")
            CHOPA.equip("copper_helmet")
            copper_helmet = 1
        if copper_boots == 0 and get_bank_item_quantity("copper_boots") > 0:
            CHOPA.bank_withdraw_item("copper_boots")
            CHOPA.equip("copper_boots")
            copper_boots = 1
        if copper_pickaxe == 0 and get_bank_item_quantity("copper_pickaxe") > 0:
            CHOPA.bank_withdraw_item("copper_pickaxe")
            CHOPA.equip("copper_pickaxe")
            copper_pickaxe = 1
        if copper_axe == 0 and get_bank_item_quantity("copper_axe") > 0:
            CHOPA.bank_withdraw_item("copper_axe")
            CHOPA.equip("copper_axe")
            copper_axe = 1
        if copper_dagger == 0 and get_bank_item_quantity("copper_dagger") > 0:
            CHOPA.bank_withdraw_item("copper_dagger")
            CHOPA.equip("copper_dagger")
            copper_dagger = 1

    while CHOPA.get_character()["gearcrafting_level"] < 10:
        if copper_armor == 0 and get_bank_item_quantity("copper_armor") > 0:
            CHOPA.bank_withdraw_item("copper_armor")
            CHOPA.equip("copper_armor")
            copper_armor = 1
        if copper_legs_armor == 0 and get_bank_item_quantity("copper_legs_armor") > 0:
            CHOPA.bank_withdraw_item("copper_legs_armor")
            CHOPA.equip("copper_legs_armor")
            copper_legs_armor = 1
        if water_bow == 0 and get_bank_item_quantity("water_bow") > 0:
            CHOPA.bank_withdraw_item("water_bow")
            water_bow = 1
        if sticky_sword == 0 and get_bank_item_quantity("sticky_sword") > 0:
            CHOPA.bank_withdraw_item("sticky_sword")
            sticky_sword = 1
        CHOPA.auto_craft("feather_coat", recycle=True)

