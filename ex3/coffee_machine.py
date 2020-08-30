import sys

water = 400
milk = 540
coffee = 120
cups = 9
money = 550


def print_all():
    """
    funtion print all ingrediant
    water, milk, coffee, cups, and money
    """
    print("=" * 25)
    print("The coffee machine has:")
    print(f"{water} of water")
    print(f"{milk} of milk")
    print(f"{coffee} of coffee beans")
    print(f"{cups} of disposable cups")
    print(f"{money} of money")
    print("=" * 25)

def check_int(b):
    """
    funtion that input how many user want to add ingredaint into coffee machine
    and check it is an integer or not if it isn't ask user again 
    """
    while True:
        # user input how many user want to add
        a = input(f"Write how many {b} do you want to add: ")
        # try to convert user input into an integer
        try:
            a = int(a)
            return a
        # if it not integer ask user again
        except ValueError:
            print("<=>" * 15)
            print("Please Enter number only.")
            print("<=>" * 15)

def buy_coffee():
    """
    function that ask user what do you want to buy 
    with 3 option to choose from is 1. espresso, 2. latte, and 3, cappuccino
    and calculate remaining amount of water milk coffee and cups
    """

    # set all local valuable into gobal (water, milk, coffee, cups) 
    global water, milk, coffee, cups

    # input loop
    while True:
        # input user's option
        print("What do you want to buy.")
        print("MENU 1-espresso 2-latte 3-cappuccino")
        user_coffee = input("Enter number 1-3 >>>")

        # if user choose 1 which is espresso
        if user_coffee == "1":
            '''
            check that all ingredaint are sufficient or not
            if it's sufficient return money
            if it's not tell user amount is missing and break out of loop
            '''
            if water >= 250 and coffee >= 16 and cups >= 1:
                water -= 250
                coffee -= 16
                cups -= 1
                return 4
            else:
                print("\n" * 5)
                print("ERROR " * 5)
                print("Fill water to 250 ml")
                print("Fill coffee beans to 16 g")
                print("Add more cup")
                break

        # if user choose 2 which is latte
        elif user_coffee == "2":
            if water >= 350 and milk >= 75 and coffee >= 20 and cups >= 1:
                water -= 350
                milk -= 75
                coffee -= 20
                cups -= 1
                return 7
            else:
                print("\n" * 5)
                print("ERROR " * 5)
                print("Fill water to 350 ml")
                print("Fill milf to 75 ml")
                print("Fill coffee beans to 20 g")
                print("Add more cup")
                break
        # if user choose 3 which is cappuccino
        elif user_coffee == "3":
            if water >= 200 and milk >= 100 and coffee >= 12 and cups >= 1:
                water -= 200
                milk -= 100
                coffee -= 12
                cups -= 1
                return 6

            else:
                print("\n" * 5)
                print("ERROR " * 5)
                print("Fill water to 200 ml")
                print("Fill milf to 100 ml")
                print("Fill coffee beans to 12 g")
                print("Add more cup")
                break

        else:
            print("\n" * 5)
            print("ERROR " * 5)
            print("<=>" * 15)
            print("Please enter number 1-3")
            print("<=>" * 15)

while True:
    # print all ingredient
    print_all()
    # ask user what user want to do
    print("+=+" * 5)
    print("Buy  Fill  Take")
    print("+=+" * 5)
    print("or you want to shut down press X")
    user_d = input("Write an action: ")

    # add ingredient into coffee machine
    if user_d.lower() == "fill":
        print("\n" * 5)
        water += check_int("ml of water")
        milk += check_int("ml of milk")
        coffee += check_int("grams of coffee beans")
        cups += check_int("disposable cup of coffee")
        print("\n" * 5)
    # buy coffee
    elif user_d.lower() == "buy":
        print("\n" * 5)
        try:
            money += int(buy_coffee())
            print("\n" * 5)
        except TypeError:
            continue
    # take money out
    elif user_d.lower() == "take":
        print(f"I give you ${money}")
        money = 0
        print("\n" * 5)

    # exit
    elif user_d.lower() == "x":
        print("Exit Exit Exit Exit Exit Exit\n" * 10)
        sys.exit()

    else:
        print("\n" * 5)





