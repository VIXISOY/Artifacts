from Source.BASE import *

if __name__ == '__main__':
  KRYST.auto_craft("slime_shield")
  KRYST.bank_deposit_item("slime_shield",1)
  KRYST.bank_deposit_full_inventory()

  while True:
    KRYST.farm_item("pig_skin")
    KRYST.bank_deposit_item("pig_skin",KRYST.get_item_quantity("pig_skin"))

  while True :
    KRYST.auto_craft_self_only("forest_whip")
    KRYST.recycle("forest_whip")
    KRYST.bank_deposit_full_inventory(["king_slimeball","wolf_hair","ogre_eye","hardwood_plank"])