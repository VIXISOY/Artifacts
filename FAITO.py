from BASE import *

heal_item = "cooked_gudgeon"
heal_amount = 75
quantity = 50
enemy = "yellow_slime"

if __name__ == '__main__':
    result = {"data":{"characters":[{"level":0}]}} #dummy result to enter the loop
    while result["data"]["characters"][0]["level"] < 4:
        current_amount = CHILD.get_item_quantity(heal_item)
        if current_amount == 0:
            CHILD.bank_deposit_full_inventory()
            CHILD.bank_withdraw_item(heal_item, min(get_bank_item_quantity(heal_item), quantity))
            if CHILD.get_item_quantity(heal_item) == 0:
                break #no more food
        info = CHILD.get_character()
        missing_health = info["max_hp"]-info["hp"]
        if missing_health > heal_amount:
            CHILD.use(heal_item,min(missing_health//heal_amount, quantity))
        CHILD.rest()
        result =CHILD.fight(enemy) 
