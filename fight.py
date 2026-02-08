import BASE
import sys

enemy = sys.argv[1] if len(sys.argv) > 1 else None
if not enemy:
    print("Please provide an enemy name as an argument.")
    sys.exit(1)
while True:
    BASE.BAGAR.careful_fight(enemy)