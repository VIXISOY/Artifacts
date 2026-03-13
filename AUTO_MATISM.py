from Source.BASE import *

if __name__ == '__main__':
  while get_bank_item_quantity("steel_helm") < 4 :
    CHILD.auto_craft_self_only("steel_helm")
    CHILD.bank_deposit_item("steel_helm")

  while get_bank_item_quantity("steel_armor") < 4 :
    CHILD.auto_craft_self_only("steel_armor")
    CHILD.bank_deposit_item("steel_armor")

  while get_bank_item_quantity("leg_armor") < 4 :
    CHILD.auto_craft_self_only("leg_armor")
    CHILD.bank_deposit_item("leg_armor")
  
  while get_bank_item_quantity("lucky_wizard_hat") < 4 :
    CHILD.auto_craft("lucky_wizard_hat")

  while True :
    CHILD.auto_craft_self_only("lucky_wizard_hat")
    CHILD.recycle("lucky_wizard_hat")
    CHILD.bank_deposit_full_inventory(["green_cloth","flying_wing","snakeskin"])
