from Source.BASE import *

if __name__ == '__main__':
  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.bank_deposit_item("greater_wooden_staff",2)

  while True :
    KRYST.auto_craft_self_only("greater_wooden_staff")
    KRYST.recycle("greater_wooden_staff")
    KRYST.bank_deposit_full_inventory(["spruce_plank","blue_slimeball"])