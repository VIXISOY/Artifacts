from Source.BASE import *

if __name__ == '__main__':

    while CHOPA.get_character()["gearcrafting_level"] < 5:
        CHOPA.auto_craft("wooden_shield", recycle=True)

    copper_armor = 0
    copper_legs_armor = 0
    water_bow = 0
    sticky_sword = 0
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

