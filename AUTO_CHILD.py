from Source.BASE import *

if __name__ == '__main__':

  while get_bank_item_quantity("piggy_helmet") < 3:
    CHILD.auto_craft("piggy_helmet")

  while True:
    CHILD.auto_craft("piggy_helmet", recycle=True)