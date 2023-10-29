menu = {"latte":{"ingredients":{"water":60, "milk" : 100, "coffee": 100},"cost" : 150},
"espresso":{"ingredients":{"water":50, "milk" : 50, "coffee": 20},"cost" : 50},
"cappuccino":{"ingredients":{"water":150, "milk" : 70, "coffee": 80},"cost" : 170}}
profit= 0 
resources = {"water" : 500, "milk": 200,  "coffee" : 200}


def check_resources(coffee_ingredients):
    for i in coffee_ingredients:
        if coffee_ingredients[i]>resources[i]:
            print(f"Sorry we do not have enough {i}")
            return False
        return True
        
def process_coins():
    print("Please insert Coins.")
    total = 0 
    coins_five = int(input("How many 5rs Coin? : "))
    coins_ten = int( input("How many 10rs Coin? : "))
    coins_twenty = int(input("How many 20rs Coins? :"))
    total = coins_five*5+ coins_ten*10 + coins_twenty*20 
    return total  
def is_payment_successful(money_received, coffee_cost):
    if money_received >= coffee_cost:
        global profit 
        profit += coffee_cost
        change = money_received - coffee_cost

        print(f"Here is your Rs{change} in change ")
        return True 
    
    else : 
        print(" Sorry that's not enough money. Money Refunded")
        return False 


def make_coffee(coffee_name ,ingredients):
    for i in ingredients:
        resources[i] -= ingredients[i]
    print(f"Here is your {coffee_name}")    

is_on = True

while is_on:
    choice = input("What would you like to have? (latte/espresso/cappuccino): ")
    if choice == "off":
        is_on = False 
    elif choice == "report":
        print(f"Water = {resources['water']}ml")
        print(f"Milk = {resources['milk']}ml")
        print(f"Coffee= {resources['coffee']}ml")
        print(f"Money = {profit}rs")
    else:
        coffee_type = menu[choice]
        print(coffee_type)
        if check_resources(coffee_type['ingredients']):
            payment = process_coins()
            if is_payment_successful(payment,coffee_type["cost"]):
                make_coffee(choice,coffee_type[ "ingredients"])



 
