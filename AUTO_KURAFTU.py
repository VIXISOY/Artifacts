from Source.BASE import *

def old():
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
    while True:
        CHILD.auto_craft_self_only("copper_legs_armor")
        CHILD.recycle("copper_legs_armor", trigger)
        current += 1
        if current == 10:
            CHILD.bank_deposit_full_inventory()
            current = 0

if __name__ == '__main__':
        BAGAR.auto_craft("greater_wooden_staff",4)
        BAGAR.auto_craft("iron_pickaxe",4)
        BAGAR.auto_craft("iron_axe",4)
        BAGAR.auto_craft("spruce_fishing_rod") 
        BAGAR.auto_craft("leather_gloves") 
