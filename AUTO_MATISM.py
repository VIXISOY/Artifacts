from Source.BASE import *

if __name__ == '__main__':
    CHILD.fighting_smart = True
    CHILD.bank_withdraw_item("spruce_plank",6)
    CHILD.auto_craft_self_only("adventurer_helmet",2)
    CHILD.bank_deposit_full_inventory()
    CHILD.bank_withdraw_item("spruce_plank",8)
    CHILD.auto_craft_self_only("adventurer_vest",2)
    CHILD.bank_deposit_full_inventory()
    CHILD.auto_craft_self_only("iron_shield",2)
    CHILD.bank_deposit_full_inventory()
    while CHILD.get_item_quantity("forest_ring") < 1:
      CHILD.farm_item("forest_ring")
    CHILD.equip("forest_ring")
    CHILD.bank_deposit_full_inventory()