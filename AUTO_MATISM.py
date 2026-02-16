from Source.BASE import *

if __name__ == '__main__':
  CHILD.auto_craft("satchel",5)
  CHILD.bank_deposit_full_inventory()
  while True:
    CHILD.auto_craft_self_only("iron_boots")
    CHILD.recycle("iron_boots")
    CHILD.bank_deposit_full_inventory(["feather","iron_bar"])
