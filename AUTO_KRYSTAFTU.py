from Source.BASE import *

if __name__ == '__main__':
  KRYST.auto_craft_self_only("water_bow",4)
  KRYST.bank_deposit_item("water_bow",3)

  sticky_sword = 0
  copper_legs_armor = 0
  copper_armor = 0
  while KRYST.get_character()["gearcrafting_level"] < 10:
    if sticky_sword == 0 and  get_bank_item_quantity("sticky_sword") > 0:
      CHILD.bank_withdraw_item("sticky_sword")
      sticky_sword = 1

    if copper_legs_armor == 0 and  get_bank_item_quantity("copper_legs_armor") > 0:
      KRYST.bank_withdraw_item("copper_legs_armor")
      KRYST.equip("copper_legs_armor")
      copper_legs_armor = 1

    if copper_armor == 0 and  get_bank_item_quantity("copper_armor") > 0:
      KRYST.bank_withdraw_item("copper_armor")
      KRYST.equip("copper_armor")
      copper_armor = 1

    KRYST.auto_craft_self_only("water_bow")
    KRYST.recycle("water_bow")
    KRYST.bank_deposit_full_inventory(["ash_plank","blue_slimeball"])

  while CHILD.get_character()["woodcutting_level"] < 10 :
    CHILD.farm_item("ash_plank",6)
    CHILD.bank_deposit_full_inventory()

  KRYST.auto_craft_self_only("greater_wooden_staff",4)
  KRYST.bank_deposit_item("greater_wooden_staff",3)

while True :
    CHILD.auto_craft_self_only("greater_wooden_staff")
    CHILD.recycle("greater_wooden_staff")
    CHILD.bank_deposit_full_inventory(["spruce_plank","blue_slimeball"])