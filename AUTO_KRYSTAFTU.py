from Source.BASE import *

if __name__ == '__main__':
  while get_bank_item_quantity("mushstaff") < 4:
    KRYST.auto_craft_self_only("mushstaff")
    KRYST.bank_deposit_item("mushstaff")
    KRYST.bank_deposit_full_inventory(["spruce_plank,mushroom,green_cloth,jasper_crystal,tasks_coin"])

  while get_bank_item_quantity("mushmush_bow") < 4:
    KRYST.auto_craft_self_only("mushmush_bow")
    KRYST.bank_deposit_item("mushmush_bow")
    KRYST.bank_deposit_full_inventory(["spruce_plank,wolf_hair,mushroom,jasper_crystal,tasks_coin"])

  while True :
    KRYST.auto_craft_self_only("mushmush_bow")
    KRYST.recycle("mushmush_bow")
    KRYST.bank_deposit_full_inventory(["spruce_plank,wolf_hair,mushroom,jasper_crystal,tasks_coin"])