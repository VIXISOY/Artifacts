from Source.BASE import *

if __name__ == '__main__':
  CHILD.bank_deposit_item("cooked_gudgeon",4)
  CHILD.bank_withdraw_item("wooden_shield")
  CHILD.equip("wooden_shield")
  
  CHILD.auto_craft_self_only("copper_legs_armor")
  CHILD.bank_deposit_item("copper_legs_armor")
  CHILD.auto_craft_self_only("copper_legs_armor")
  CHILD.bank_deposit_item("copper_legs_armor")
  CHILD.auto_craft_self_only("copper_legs_armor")
  CHILD.bank_deposit_item("copper_legs_armor")
  CHILD.auto_craft_self_only("copper_legs_armor")
  CHILD.equip("copper_legs_armor")
  CHILD.bank_deposit_full_inventory()

  CHILD.auto_craft_self_only("copper_armor")
  CHILD.bank_deposit_item("copper_armor")
  CHILD.auto_craft_self_only("copper_armor")
  CHILD.bank_deposit_item("copper_armor")
  CHILD.auto_craft_self_only("copper_armor")
  CHILD.bank_deposit_item("copper_armor")
  CHILD.auto_craft_self_only("copper_armor")
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

  CHILD.auto_craft_self_only("iron_boots")
  CHILD.bank_deposit_item("iron_boots")
  CHILD.auto_craft_self_only("iron_boots")
  CHILD.bank_deposit_item("iron_boots")
  CHILD.auto_craft_self_only("iron_boots")
  CHILD.bank_deposit_item("iron_boots")
  CHILD.auto_craft_self_only("iron_boots")
  CHILD.equip("iron_boots")

  CHILD.bank_deposit_full_inventory()
  CHILD.auto_craft_self_only("iron_armor")
  CHILD.bank_deposit_item("iron_armor")
  CHILD.auto_craft_self_only("iron_armor")
  CHILD.bank_deposit_item("iron_armor")
  CHILD.auto_craft_self_only("iron_armor")
  CHILD.bank_deposit_item("iron_armor")
  CHILD.auto_craft_self_only("iron_armor")
  CHILD.equip("iron_armor")
  CHILD.bank_deposit_full_inventory()
  
  CHILD.auto_craft_self_only("iron_legs_armor")
  CHILD.bank_deposit_item("iron_legs_armor")
  CHILD.auto_craft_self_only("iron_legs_armor")
  CHILD.bank_deposit_item("iron_legs_armor")
  CHILD.auto_craft_self_only("iron_legs_armor")
  CHILD.bank_deposit_item("iron_legs_armor")
  CHILD.auto_craft_self_only("iron_legs_armor")
  CHILD.equip("iron_legs_armor")
  CHILD.bank_deposit_full_inventory()

  while True :
    CHILD.auto_craft_self_only("iron_boots")
    CHILD.recycle("iron_boots")
    CHILD.bank_deposit_full_inventory(["iron_bar","feather"])
