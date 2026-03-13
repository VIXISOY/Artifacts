from Source.BASE import *

if __name__ == '__main__':
  while get_bank_item_quantity("steel_helm") < 4 :
    CHILD.auto_craft_self_only("steel_helm")
    CHILD.bank_deposit_item("steel_helm")

  while get_bank_item_quantity("steel_armor") < 4 :
    CHILD.auto_craft_self_only("steel_armor")
    CHILD.bank_deposit_item("steel_armor")

  while get_bank_item_quantity("hard_leather_pants") < 4 :
    CHILD.auto_craft_self_only("hard_leather_pants")
    CHILD.bank_deposit_item("hard_leather_pants")

  while True :
    CHILD.auto_craft_self_only("steel_helm")
    CHILD.recycle("steel_helm")
    CHILD.bank_deposit_full_inventory(["steel_bar","ogre_skin","wolf_bone","cloth"])
