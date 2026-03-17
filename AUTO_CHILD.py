from Source.BASE import *

if __name__ == '__main__':

  while get_bank_item_quantity("skeleton_armor") < 4:
    CHILD.auto_craft("skeleton_armor")

  while get_bank_item_quantity("skeleton_pants") < 4:
    CHILD.auto_craft("skeleton_pants")

  while get_bank_item_quantity("tromatising_mask-pants") < 4:
    CHILD.auto_craft("tromatising_mask")

  while True:
    CHILD.auto_craft_self_only("hard_leather_pants")
    CHILD.recycle("hard_leather_pants")
    CHILD.bank_deposit_full_inventory(["steel_bar","green_cloth","hard_leather","skeleton_skull"])