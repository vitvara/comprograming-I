import sys

water = 3
milk = 2
coffee = 1
cups = 0
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
                print("I CAN'T MAKE CUP OF COFFEE")
                resource_remain(250, 0, 16, 1)
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
                print("I CAN'T MAKE CUP OF COFFEE")
                resource_remain(350, 75, 20, 1)
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
                print("I CAN'T MAKE CUP OF COFFEE")
                resource_remain(200, 100, 12, 1)
                break

        else:
            print("\n" * 5)
            print("ERROR " * 5)
            print("<=>" * 15)
            print("Please enter number 1-3")
            print("<=>" * 15)

def resource_remain(w, m, coff, cup_):
    """
    funtion that calculate how many coffee machine need to add
    """
    global water, milk, coffee, cups
    remaining_list = [water, milk ,coffee, cups]
    needed_list = [w, m, coff, cup_]
    name_resource = ["water", "milk", "coffee", "cup"]
    # check unit
    for i in range(len(remaining_list)):
        if needed_list[i] > remaining_list[i]:
            if remaining_list[i] in [water, milk]:
                print(f"Please fill {name_resource[i]} more than {needed_list[i] - remaining_list[i]} ml")
            elif remaining_list[i] in [coffee]:
                print(f"Please fill coffee beans to {needed_list[i] - remaining_list[i]} g")
            elif remaining_list[i] in [cups]:
                print(f"Please fill up to {needed_list[i] - remaining_list[i]} cups")
        

def action_():
    """
    funtion choose action
    """
    global water, milk, coffee, cups, money
    while True:
        print("+=+" * 10)
        print("Buy  Fill  Take Remaining Exit")
        print("+=+" * 10)

        user_d = input("Write an action: ")

        # print all resource
        if user_d.lower() == "remaining":
            print("\n" * 5)
            print_all()
            

        # fill resource
        elif user_d.lower() == "fill":
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
        elif user_d.lower() == "exit":
            print("Exit Exit Exit Exit Exit Exit\n" * 10)
            sys.exit()
        
        else:
            print("\n" * 5)

        # add ingredient into coffee machine

action_()






