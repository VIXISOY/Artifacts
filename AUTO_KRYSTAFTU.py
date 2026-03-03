from Source.BASE import *

if __name__ == '__main__':
  KRYST

  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.bank_deposit_item("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.bank_deposit_item("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")
  CHILD.bank_deposit_full_inventory(["spruce_plank","blue_slimeball"])

while True :
    CHILD.auto_craft_self_only("greater_wooden_staff")
    CHILD.recycle("greater_wooden_staff")
    CHILD.bank_deposit_full_inventory(["spruce_plank","blue_slimeball"])