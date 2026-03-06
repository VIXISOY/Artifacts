from Source.BASE import *

if __name__ == '__main__':

  CHILD.auto_craft_self_only("iron_shield")
  CHILD.bank_deposit_item("iron_shield")
  CHILD.auto_craft_self_only("iron_shield")
  CHILD.bank_deposit_item("iron_shield")
  CHILD.auto_craft_self_only("iron_shield")
  CHILD.bank_deposit_item("iron_shield")
  CHILD.auto_craft_self_only("iron_shield")
  CHILD.equip("iron_shield")
  CHILD.bank_deposit_full_inventory()

  while True :
    CHILD.auto_craft_self_only("lucky_wizard_hat")
    CHILD.recycle("lucky_wizard_hat")
    CHILD.bank_deposit_full_inventory(["green_cloth","flying_wing","snakeskin"])
