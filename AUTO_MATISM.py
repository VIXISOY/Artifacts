from Source.BASE import *

if __name__ == '__main__':
    current = 0
    trigger = 10
    CHILD.bank_deposit_full_inventory()
    while True:
      CHILD.auto_craft_self_only("copper_legs_armor")
      CHILD.bank_deposit_full_inventory()
      current+=1
      if current == trigger:
        CHILD.bank_withdraw_item("copper_legs_armor", trigger)
        CHILD.recycle("copper_legs_armor",trigger)
        CHILD.bank_deposit_full_inventory()
        current = 0
    