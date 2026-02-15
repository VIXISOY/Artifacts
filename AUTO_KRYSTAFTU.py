from Source.BASE import *

if __name__ == '__main__':
    #KRYST.fighting_smart = True
    #for i in range(10):
    
    while KRYST.get_character()["weaponcrafting_level"] < 5:
        KRYST.bank_deposit_full_inventory(["feather"])
        KRYST.auto_craft_self_only("apprentice_gloves")
        KRYST.recycle("apprentice_gloves")
    while KRYST.get_character()["weaponcrafting_level"] < 10:
        KRYST.bank_deposit_full_inventory(["blue_slimeball","ash_plank"])
        KRYST.auto_craft_self_only("water_bow")
        KRYST.recycle("water_bow")
    while True:
        KRYST.bank_deposit_full_inventory(["blue_slimeball","spruce_plank"])
        KRYST.auto_craft_self_only("greater_wooden_staff")
        KRYST.recycle("greater_wooden_staff")


        
