from Source.BASE import *

if __name__ == '__main__':
    
    BAGAR.bank_deposit_full_inventory()
    count = 4
    while True:
        BAGAR.auto_craft("fire_staff")
        BAGAR.recycle("fire_staff")

        count += 1

        if count == 5:
            BAGAR.bank_deposit_full_inventory()
            count = 0

    current = 10