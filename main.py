from sys import exit

# TODO 1:prompt user by asking.
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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}
money = 0.00
# TODO 3: print report


def report():
    water = resources["water"]
    milk = resources["milk"]
    coffee = resources["coffee"]

    return f"Water: {water}ml\nMilk: {milk}ml\nCoffee: {coffee}g\nMoney: ${money}"
# TODO 4: Check resource sufficient


def sufficient(drink):

    if drink == "espresso":
        if MENU["espresso"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"]:
            return 0
        elif MENU["espresso"]["ingredients"]["water"] > resources["water"]:
            return "Sorry, there is not enough water"
        elif MENU["espresso"]["ingredients"]["coffee"] > resources["coffee"]:
            return "Sorry, there is not enough coffee"
    elif drink == "latte":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
            return 0
        elif MENU["latte"]["ingredients"]["water"] > resources["water"]:
            return "Sorry, there is not enough water"
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            return "Sorry, there is not enough coffee"
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            return "Sorry, there is not enough milk"
    elif drink == "cappuccino":
        if MENU["latte"]["ingredients"]["water"] <= resources["water"] and MENU["espresso"]["ingredients"]["coffee"] <= resources["coffee"] and MENU["latte"]["ingredients"]["milk"] <= resources["milk"]:
            return 0
        elif MENU["latte"]["ingredients"]["water"] > resources["water"]:
            return "Sorry, there is not enough water"
        elif MENU["latte"]["ingredients"]["coffee"] > resources["coffee"]:
            return "Sorry, there is not enough coffee"
        elif MENU["latte"]["ingredients"]["milk"] > resources["milk"]:
            return "Sorry, there is not enough milk"


def process_coins():
    quarters1 = int(input("Enter number of quarters: "))
    dimes1 = int(input("Enter number of dimes: "))
    nickles1 = int(input("Enter number of quarters: "))
    pennies1 = int(input("Enter number of quarters: "))

    quarters = float(quarters1 * 0.25)
    dimes = float(dimes1 * 0.10)
    nickles = float(nickles1 * 0.05)
    pennies = float(pennies1 * 0.01)

    total = quarters + dimes + nickles + pennies
    return round(total, 2)


def make_coffee(make):
    if make == "espresso":
        resources['water'] -= MENU["espresso"]["ingredients"]["water"]
        resources["coffee"] -= MENU["espresso"]["ingredients"]["coffee"]
        return "Successful!!. Enjoy your Espresso"

    elif make == "latte":
        resources["water"] -= MENU["latte"]["ingredients"]["water"]
        resources["milk"] -= MENU["latte"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["latte"]["ingredients"]["coffee"]
        return "Successful!!. Enjoy your Latte"

    elif make == "cappuccino":
        resources["water"] -= MENU["cappuccino"]["ingredients"]["water"]
        resources["milk"] -= MENU["cappuccino"]["ingredients"]["milk"]
        resources["coffee"] -= MENU["cappuccino"]["ingredients"]["coffee"]
        return "Successful!!. Enjoy your Cappuccino"


def coffee_maker():
    turn_off = False
    user_done = False
    global money
    while not turn_off:
        user_data = input("What would you like? (espresso/latte/cappuccino/report\n").lower()
        if user_data == "report":
            print(report())
            turn_off = True
        elif user_data == "off":
            exit()
        elif user_data == "espresso":
            data = sufficient("espresso")
            if data == 0:
                print("Kindly pay a total of $1.5")
                amount = process_coins()
                while not user_done:
                    if amount == MENU["espresso"]["cost"]:
                        money += amount
                        print(f"You have provided a total of total ${amount}")
                        print(make_coffee(user_data))
                        user_done = True
                        turn_off = True

                    elif amount > MENU["espresso"]["cost"]:
                        refund = round((amount - MENU["espresso"]["cost"]), 2)
                        money += round((MENU["espresso"]["cost"]), 2)

                        print(f"You have provided a total of total ${amount} and your change is ${refund}.")
                        print(make_coffee(user_data))
                        user_done= True
                        turn_off = True

                    else:
                        done = input("The amount entered is not sufficient. Refund of the same has been done. 'continue' or 'exit': ")
                        if done == "continue":
                            user_done = False
                        else:
                            user_done= True
                            turn_off = True
            else:
                print(data)
                turn_off = True
        elif user_data == "latte":
            data = sufficient("latte")
            if data == 0:
                print("Kindly pay a total of $2.5")
                amount = process_coins()
                while not user_done:
                    if amount == MENU["latte"]["cost"]:
                        money += amount

                        print(f"You have provided a total of total ${amount}")
                        print(make_coffee(user_data))
                        user_done= True
                        turn_off = True

                    elif amount > MENU["latte"]["cost"]:
                        refund = round((amount - MENU["latte"]["cost"]), 2)
                        money += round((amount - MENU["latte"]["cost"]), 2)

                        print(f"You have provided a total of ${amount} and your change is ${refund}.")
                        print(make_coffee(user_data))
                        user_done= True
                        turn_off = True

                    else:
                        done = input("The amount entered is not sufficient. Refund of the same has been done. 'continue' or 'exit': ")
                        if done == "continue":
                            user_done = False
                        else:
                            user_done= True
                            turn_off = True

            else:
                print(data)
                turn_off = True
        elif user_data == "cappuccino":
            data = sufficient("cappuccino")
            if data == 0:
                print("Kindly pay a total of $3.0")
                amount = process_coins()
                while not user_done:
                    if amount == MENU["cappuccino"]["cost"]:
                        money += amount

                        print(f"You have provided a total of total ${amount}")
                        print(make_coffee(user_data))
                        user_done= True
                        turn_off = True

                    elif amount > MENU["cappuccino"]["cost"]:
                        refund = round((amount - MENU["cappuccino"]["cost"]), 2)
                        money += round((MENU["cappuccino"]["cost"]), 2)

                        print(f"You have provided a total of total ${amount} and your change is ${refund}.")
                        print(make_coffee(user_data))
                        user_done= True
                        turn_off = True

                    else:
                        done = input("The amount entered is not sufficient. Refund of the same has been done. 'continue' or 'exit': ")
                        if done == "continue":
                            user_done = False
                        else:
                            user_done= True
                            turn_off = True

            else:
                print(data)
                turn_off = True

        else:
            print("You have entered wrong information. Lets try again")
            turn_off = False

    main()


def main():
    cont = input("Welcome, Do you want to make some coffee? Respond with either 'yes' or 'no': ").lower()
    if cont == "yes":
        coffee_maker()
    else:
        print("Enjoy your time")
        exit()


main()









