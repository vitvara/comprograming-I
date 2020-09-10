import  sys
water = 400
milk = 540
coffee_beans = 120
disposable_cups = 9
money = 550

def print_all():
    print("The coffee machine: ")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")
    print("")


def choose_action():
    action = input("Write action (buy, fill, take, remaining, exit): ")
    if action == "buy":
        return buy_coffee()
    elif action == "fill":
        return fill_ingredient()
    elif action == "take":
        return take_money()
    elif action == "remaining":
        return remain_menu()
    elif action == "exit":
        sys.exist



def buy_coffee():
    global water, milk, coffee_beans, disposable_cups, money
    while True:
        type_coffee = int(input("What do you want to buy(1 - espresso, 2 - latte, 3 - cappuccino): > "))
        if type_coffee == 1:
            water -= 250
            coffee_beans -= 16
            disposable_cups -= 1
            money += 4
            print("")
            break

        elif type_coffee == 2:
            water -= 350
            milk -= 75
            coffee_beans -= 20
            disposable_cups -= 1
            money += 7
            print("")
            break

        elif type_coffee == 3:
            water -= 200
            milk = -100
            coffee_beans -= 12
            disposable_cups -= 1
            money += 6
            print("")
            break

        else:
            print("Please enter only 1-3")


def fill_ingredient():
    global water, milk, coffee_beans, disposable_cups, money
    fill_water = int(input("Write how many ml of water do you want add: "))
    fill_milk = int(input("Write how many ml of milk do you want add: "))
    fill_coffee_beans = int(input("Write how many grams of coffee beans do you want add: "))
    fill_cups = int(input("Write how many disposable cups of coffee do you want add: "))
    water += fill_water
    milk += fill_milk
    coffee_beans += fill_coffee_beans
    disposable_cups += fill_cups
    print("")
    print(remain_menu())



def take_money():
    global money
    print(f"I gave you ${money}")
    money -= money
    print("")
    print(remain_menu())


def remain_menu():
    print("The coffee machine: ")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee_beans} of coffee beans")
    print(f"{disposable_cups} of disposable cups")
    print(f"{money} of money")
    print("")


while True:
    print_all()
    choose_action()