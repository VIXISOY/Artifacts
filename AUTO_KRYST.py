from Source.BASE import *
KRYST = Character("KRYST")

if __name__ == '__main__':
  while True:
    KRYST.farm_item("tasks_coin")
    KRYST.bank_deposit_item("tasks_coin",KRYST.get_item_quantity("tasks_coin"))