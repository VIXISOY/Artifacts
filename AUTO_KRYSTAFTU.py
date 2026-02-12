from Source.BASE import *

if __name__ == '__main__':
        #for i in range(10):
        while KRYST.get_character()["alchemy_level"] < 20:
            KRYST.auto_craft("small_health_potion",30)
        while True:
              KRYST.farm_item("nettle_leaf",80)
        
