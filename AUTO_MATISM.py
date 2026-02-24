from Source.BASE import *

if __name__ == '__main__':
  CHILD.auto_craft_self_only("copper_boots",4)
  CHILD.equip("copper_boots")
  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("copper_helmet",4)
  CHILD.equip("copper_helmet")
  CHILD.bank_deposit_full_inventory()

  copper_pickaxe = 0
  copper_axe = 0
  copper_dagger = 0
  wooden_shield = 0
  while CHILD.get_character()["gearcrafting_level"] < 5:
    if copper_pickaxe == 0 and  get_bank_item_quantity("copper_pickaxe") > 0:
      CHILD.bank_withdraw_item("copper_pickaxe")
      copper_pickaxe = 1

    if copper_axe == 0 and  get_bank_item_quantity("copper_axe") > 0:
      CHILD.bank_withdraw_item("copper_axe")
      copper_axe = 1

    if copper_dagger == 0 and  get_bank_item_quantity("copper_dagger") > 0:
      CHILD.bank_withdraw_item("copper_dagger")
      copper_dagger = 1
    
    if wooden_shield == 0 and  get_bank_item_quantity("wooden_shield") > 0:
      KRYST.bank_withdraw_item("wooden_shield")
      KRYST.equip("wooden_shield")
      wooden_shield = 1

    CHILD.auto_craft_self_only("copper_helmet")
    CHILD.recycle("copper_helmet")
    CHILD.bank_deposit_full_inventory(["copper_bar"])
  
  CHILD.auto_craft_self_only("copper_legs_armor",4)
  CHILD.equip("copper_legs_armor")
  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("copper_armor",4)
  CHILD.equip("copper_armor")
  CHILD.bank_deposit_full_inventory()

  sticky_sword = 0
  water_bow = 0
  while CHILD.get_character()["gearcrafting_level"] < 10:
    if sticky_sword == 0 and  get_bank_item_quantity("sticky_sword") > 0:
      CHILD.bank_withdraw_item("sticky_sword")
      sticky_sword = 1
      
    if water_bow == 0 and  get_bank_item_quantity("water_bow") > 0:
      CHILD.bank_withdraw_item("water_bow")
      water_bow = 1
    
    CHILD.auto_craft_self_only("copper_legs_armor")
    CHILD.recycle("copper_legs_armor")
    CHILD.bank_deposit_full_inventory(["copper_bar","feather"])

  while CHILD.get_character()["mining_level"] < 10 :
    CHILD.farm_item("copper_bar",6)
    CHILD.bank_deposit_full_inventory()

  CHILD.auto_craft_self_only("iron_boots",4)
  CHILD.equip("iron_boots")
  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("iron_armor",4)
  CHILD.equip("iron_armor")
  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("iron_legs_armor",4)
  CHILD.equip("iron_legs_armor")
  CHILD.bank_deposit_full_inventory()

  while True :
    CHILD.auto_craft_self_only("iron_boots")
    CHILD.recycle("iron_boots")
    CHILD.bank_deposit_full_inventory(["iron_bar","feather"])
