from Source.BASE import *

if __name__ == '__main__':
  CHILD.bank_deposit_full_inventory()

  CHILD.auto_craft_self_only("iron_helm")
  CHILD.bank_deposit_item("iron_helm")
  CHILD.auto_craft_self_only("iron_helm")
  CHILD.bank_deposit_item("iron_helm")
  CHILD.auto_craft_self_only("iron_helm")
  CHILD.bank_deposit_item("iron_helm")
  CHILD.auto_craft_self_only("iron_helm")
  CHILD.equip("iron_helm")

  CHILD.bank_deposit_full_inventory()
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
    CHILD.auto_craft_self_only("iron_boots")
    CHILD.recycle("iron_boots")
    CHILD.bank_deposit_full_inventory(["iron_bar","feather"])
