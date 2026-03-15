from Source.BASE import *

if __name__ == '__main__':

  while True:
    CHILD.farm_item("tasks_coin")
    CHILD.bank_deposit_item("tasks_coin",CHILD.get_item_quantity("tasks_coin"))