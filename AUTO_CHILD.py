from Source.BASE import *

if __name__ == '__main__':

  while get_bank_item_quantity("jasper_crystal") < 12:
    KRYST.farm_item("jasper_crystal")
    KRYST.bank_deposit_item("jasper_crystal",KRYST.get_item_quantity("jasper_crystal"))