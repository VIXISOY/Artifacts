from Source.BASE import *

if __name__ == '__main__':
    while CHILD.get_character()["jewelrycrafting_level"] < 5:
      CHILD.auto_craft("copper_ring")
      CHILD.recycle("copper_ring",get_bank_item_quantity("copper_ring"))
    
    while True:
      CHILD.auto_craft("copper_legs_armor")
      CHILD.recycle("copper_legs_armor",get_bank_item_quantity("copper_legs_armor"))
    