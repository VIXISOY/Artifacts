from Source.BASE import *

if __name__ == '__main__':
  while True:
    KRYST.farm_item("tasks_coin")
    KRYST.bank_deposit_item("tasks_coin",KRYST.get_item_quantity("tasks_coin"))

  while True :
    KRYST.auto_craft_self_only("forest_whip")
    KRYST.recycle("forest_whip")
    KRYST.bank_deposit_full_inventory(["king_slimeball","wolf_hair","ogre_eye","hardwood_plank"])