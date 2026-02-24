from Source.BASE import *

if __name__ == '__main__':
  KRYST.auto_craft_self_only("fishing_net")
  KRYST.bank_deposit_item("fishing_net")
  KRYST.auto_craft_self_only("wooden_staff")
  KRYST.auto_craft_self_only("apprentice_gloves")

  copper_pickaxe = 0
  copper_axe = 0
  copper_dagger = 0
  copper_boots = 0
  copper_helmet = 0
  wooden_shield = 0
  while KRYST.get_character()["gearcrafting_level"] < 5:
    if copper_pickaxe == 0 and  get_bank_item_quantity("copper_pickaxe") > 0:
      KRYST.bank_withdraw_item("copper_pickaxe")
      copper_pickaxe = 1

    if copper_axe == 0 and  get_bank_item_quantity("copper_axe") > 0:
      KRYST.bank_withdraw_item("copper_axe")
      copper_axe = 1

    if copper_dagger == 0 and  get_bank_item_quantity("copper_dagger") > 0:
      KRYST.bank_withdraw_item("copper_dagger")
      copper_dagger = 1
      
    if copper_boots == 0 and  get_bank_item_quantity("copper_boots") > 0:
      KRYST.bank_withdraw_item("copper_boots")
      KRYST.equip("copper_boots")
      copper_boots = 1

    if copper_helmet == 0 and  get_bank_item_quantity("copper_helmet") > 0:
      KRYST.bank_withdraw_item("copper_helmet")
      KRYST.equip("copper_helmet")
      copper_helmet = 1

    if wooden_shield == 0 and  get_bank_item_quantity("wooden_shield") > 0:
      KRYST.bank_withdraw_item("wooden_shield")
      KRYST.equip("wooden_shield")
      wooden_shield = 1

    KRYST.auto_craft_self_only("fishing_net")
    KRYST.recycle("fishing_net")
    KRYST.bank_deposit_full_inventory(["ash_plank"])
  
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

        
