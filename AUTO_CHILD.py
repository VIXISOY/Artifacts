from Source.BASE import *

if __name__ == '__main__':

  while True:
    CHILD.auto_craft_self_only("hard_leather_pants")
    CHILD.recycle("hard_leather_pants")
    CHILD.bank_deposit_full_inventory(["steel_bar","green_cloth","hard_leather","skeleton_skull"])