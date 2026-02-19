from Source.BASE import *

if __name__ == '__main__':
  while CHILD.get_character()["jewelrycrafting_level"] < 10:
    CHILD.auto_craft_self_only("life_amulet")
    CHILD.recycle("life_amulet")
    CHILD.bank_deposit_full_inventory(["feather","red_slimeball"])
  CHILD.auto_craft_self_only("air_and_water_amulet")
  CHILD.equip("air_and_water_amulet")
  while CHILD.get_character()["jewelrycrafting_level"] < 15:
    CHILD.auto_craft_self_only("iron_ring")
    CHILD.recycle("iron_ring")
    CHILD.bank_deposit_full_inventory(["iron_bar","wool"])
  while True:
    CHILD.auto_craft_self_only("earth_ring")
    CHILD.recycle("earth_ring")
    CHILD.bank_deposit_full_inventory(["iron_bar","yellow_slimeball","flying_wing"])
   