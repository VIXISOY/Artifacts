from Source.BASE import *

if __name__ == '__main__':
    CHILD.fighting_smart = True
    CHILD.auto_craft_self_only("adventurer_helmet")
    CHILD.equip("adventurer_helmet")
    CHILD.bank_deposit_full_inventory()
    CHILD.auto_craft_self_only("adventurer_vest")
    CHILD.equip("adventurer_vest")
    CHILD.bank_deposit_full_inventory()
    CHILD.auto_craft_self_only("iron_shield")
    CHILD.equip("iron_shield")
    CHILD.bank_deposit_full_inventory()
    while CHILD.get_item_quantity("forest_ring") < 1:
      CHILD.farm_item("forest_ring")
    CHILD.equip("forest_ring")
    CHILD.bank_deposit_full_inventory()