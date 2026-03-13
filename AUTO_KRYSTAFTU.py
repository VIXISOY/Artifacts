from Source.BASE import *

if __name__ == '__main__':
  while get_bank_item_quantity("jasper_crystal") < 7:
    KRYST.farm_item("jasper_crystal")
    KRYST.bank_deposit_item("mushstaff")
    KRYST.bank_deposit_full_inventory(["spruce_plank","mushroom","green_cloth","jasper_crystal","tasks_coin"])

  while True :
    KRYST.auto_craft_self_only("forest_whip")
    KRYST.recycle("forest_whip")
    KRYST.bank_deposit_full_inventory(["king_slimeball","wolf_hair","ogre_eye","hardwood_plank"])