from Source.BASE import *

if __name__ == '__main__':
  CHILD.fighting_smart = True
  CHILD.bank_withdraw_item("spruce_plank",8)
  CHILD.auto_craft_self_only("adventurer_vest",2)
  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("iron_shield",2)
  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("leather_legs_armor",2)
  CHILD.bank_deposit_full_inventory()

  while True:
    CHILD.bank_deposit_full_inventory()
    CHILD.auto_craft_self_only("iron_legs_armor")