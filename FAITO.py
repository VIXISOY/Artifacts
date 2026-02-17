from Source.BASE import *

heal_item = "cooked_gudgeon"
heal_amount = get(f'/items/{heal_item}')["effects"][0]["value"]
quantity = 20
enemy = "yellow_slime"

if __name__ == '__main__':
    #result = {"data":{"characters":[{"level":0}]}} #dummy result to enter the loop
    #while result["data"]["characters"][0]["level"] < 4:
        #result =CHILD.fight(enemy) 
    
    #response = post(f"/my/{CHILD.name}/action/task/complete")
    #while response == None: # task not succesfull
    #response = post(f"/my/{CHILD.name}/action/task/complete")

    heal_item = "cooked_gudgeon"
    quantity = 20
    heal_amount = get(f'/items/{heal_item}')["effects"][0]["value"]
    current_amount = CHILD.get_item_quantity(heal_item)
    if current_amount == 0:
        CHILD.bank_withdraw_item(heal_item, min(get_bank_item_quantity(heal_item), quantity))
    info = CHILD.get_character()
    missing_health = info["max_hp"]-info["hp"]
    CHILD.use(heal_item,min(missing_health//heal_amount, quantity))
    CHILD.rest()
    CHILD.fight(enemy) 
