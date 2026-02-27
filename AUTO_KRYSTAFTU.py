from Source.BASE import *

if __name__ == '__main__':

  KRYST.auto_craft_self_only("water_bow")
  CHILD.equip("water_bow")
  KRYST.auto_craft_self_only("water_bow")
  CHILD.bank_deposit_item("water_bow")
  KRYST.auto_craft_self_only("water_bow")
  CHILD.bank_deposit_item("water_bow")
  KRYST.auto_craft_self_only("water_bow")
  CHILD.bank_deposit_item("water_bow")

  while KRYST.get_character()["gearcrafting_level"] < 10:
    KRYST.auto_craft_self_only("water_bow")
    KRYST.recycle("water_bow")
    KRYST.bank_deposit_full_inventory(["ash_plank","blue_slimeball"])

  while CHILD.get_character()["woodcutting_level"] < 10 :
    CHILD.farm_item("ash_plank",6)
    CHILD.bank_deposit_full_inventory()

  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.bank_deposit_item("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.bank_deposit_item("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")
  KRYST.bank_deposit_item("greater_wooden_staff")
  KRYST.auto_craft_self_only("greater_wooden_staff")

while True :
    CHILD.auto_craft_self_only("greater_wooden_staff")
    CHILD.recycle("greater_wooden_staff")
    CHILD.bank_deposit_full_inventory(["spruce_plank","blue_slimeball"])