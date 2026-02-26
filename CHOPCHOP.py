from Source.BASE import *

if __name__ == '__main__':

    CHOPA.bank_deposit_full_inventory()

    water_bow = 0
    while CHOPA.get_character()["gearcrafting_level"] < 10:
        if water_bow == 0 and get_bank_item_quantity("water_bow") > 0:
            CHOPA.bank_withdraw_item("water_bow")
            water_bow = 1
        CHOPA.auto_craft("feather_coat", recycle=True)
        CHOPA.bank_deposit_full_inventory()

