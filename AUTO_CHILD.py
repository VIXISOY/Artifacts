from Source.BASE import *

if __name__ == '__main__':

  while get_bank_item_quantity("jasper_crystal") < 12:
    CHILD.farm_item("jasper_crystal")
    CHILD.bank_deposit_item("jasper_crystal",CHILD.get_item_quantity("jasper_crystal"))