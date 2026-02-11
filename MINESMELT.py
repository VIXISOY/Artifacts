from Source.BASE import *

ore = "iron_ore"
ingot = "iron_bar"
tool = "copper_pickaxe"
quantity = 80

if __name__ == '__main__':
    CHILD.bank_deposit_full_inventory()
    CHILD.bank_withdraw_item(tool,1)
    CHILD.equip(tool, "weapon")
    while True:
        CHILD.bank_deposit_full_inventory()
        if get_bank_item_quantity(ore) <= quantity:
            CHILD.farm_item(ore,quantity)
        CHILD.bank_deposit_full_inventory()
        CHILD.bank_withdraw_item(ore,min(get_bank_item_quantity(ore),quantity))
        CHILD.craft(ingot,CHILD.get_item_quantity(ore)//10)
