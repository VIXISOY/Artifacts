from BASE import *

quantity = 20
if __name__ == '__main__':
    response = post(f"/my/{BAGAR.name}/action/task/complete")
    while response == None: # task not succesfull
        if BAGAR.get_item_quantity("cooked_gudgeon") == 0:
            BAGAR.bank_deposit_full_inventory()
            BAGAR.bank_withdraw_item("cooked_gudgeon", min(get_bank_item_quantity("cooked_gudgeon"), quantity))
            if BAGAR.get_item_quantity("cooked_gudgeon") == 0:
                break #no more food
        info = BAGAR.get_info()
        missing_health = info["max_hp"]-info["hp"]
        if missing_health > 75:
            BAGAR.use("cooked_gudgeon")
        BAGAR.fight("chicken") 
        response = post(f"/my/{BAGAR.name}/action/task/complete")
