MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

resouces = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
    "money": 0,
}

def Check_Resources(choice):
    for ingrident in MENU[choice]['ingredients']:
        if MENU[choice]["ingredients"][ingrident] > resouces[ingrident]:
            return "Sorry there is not enough " + ingrident + "."
    return 1

def process_money():
    print("Please insert coins")
    quarters = int(input("How many quarters? "))
    dimes = int(input("How many dimes? "))
    nickels = int(input("How many nickels? "))
    pennies = int(input("How many pennies? "))
    return (quarters*25 + dimes*10 + nickels*5 + pennies)/100

def add_moeny(inserted_moeny, choice):
    if MENU[choice]["cost"] == inserted_moeny:
        print(f"Here is your {choice}. Enjoy!")
        resouces["money"] += inserted_moeny
        make_coffee(choice)
    elif MENU[choice]["cost"] < inserted_moeny:
        print(f"Here is ${(inserted_moeny - MENU[choice]["cost"]):.2f} in change.")
        print(f"Here is your {choice}. Enjoy!")
        resouces["money"] += MENU[choice]["cost"]
        make_coffee(choice)
    else:
        print("Sorry that's not enough money. Money Refunded.")

def make_coffee(choice):
    if Check_Resources(choice) == 1:
        for ing in MENU[choice]["ingredients"]:
            resouces[ing] -= MENU[choice]["ingredients"][ing]

Power_ON = True
while Power_ON:
    enough = False
    choice = input("What would you like? (espresso/latte/cappuccino)? ").lower()

    if choice == "off":
        Power_ON = False
    elif choice == "report":
        print(f"Water: {resouces["water"]}ml \nMilk: {resouces["milk"]}ml \
            \nCoffee: {resouces["coffee"]}g \nMoney: ${resouces["money"]:.2f}")
    elif choice in ["espresso", "latte", "cappuccino"]:
        enough = Check_Resources(choice)
        if enough != 1:
            print(enough)
        else:
           customer_coins = process_money()
           add_moeny(customer_coins, choice)
    else:
        print("Invalid choice. Try again.")