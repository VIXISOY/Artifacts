from Source.BASE import *

if __name__ == '__main__':
    KRYST.fight_smart = True
    #for i in range(10):
    while KRYST.get_character()["alchemy_level"] < 20:
        KRYST.auto_craft("earth_boost_potion",20)
    while True:
            KRYST.farm_item("nettle_leaf",80)
        
