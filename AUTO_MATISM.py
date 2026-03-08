from Source.BASE import *

if __name__ == '__main__':
  while get_bank_item_quantity("mushmush_wizard_hat") < 3 :
    CHILD.auto_craft_self_only("mushmush_wizard_hat")
    CHILD.bank_deposit_item("mushmush_wizard_hat")
  CHILD.auto_craft_self_only("mushmush_wizard_hat")
  CHILD.equip("mushmush_wizard_hat")

  while get_bank_item_quantity("mushmush_jacket") < 3 :
    CHILD.auto_craft_self_only("mushmush_jacket")
    CHILD.bank_deposit_item("mushmush_jacket")
  CHILD.auto_craft_self_only("mushmush_jacket")
  CHILD.equip("mushmush_jacket")

  while True :
    CHILD.auto_craft_self_only("lucky_wizard_hat")
    CHILD.recycle("lucky_wizard_hat")
    CHILD.bank_deposit_full_inventory(["green_cloth","flying_wing","snakeskin"])
