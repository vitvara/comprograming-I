"""
# input spin and charge from user
user_spin_input = input("Spin: ")
user_charge_input = input("Charge: ")

# condition to check
if user_spin_input == "1/2":
    if user_charge_input == "-1/3":
        print("Strange Quark")
    elif user_charge_input == "2/3":
        print("Charm Quark")
    elif user_charge_input == "-1":
        print("Electron Lepton")
    elif user_charge_input == "0":
        print("Neutrino Lepton")
elif user_spin_input == "1":
    print("Photon Boson")

"""

"""
# Calculator
# input a, b and operator
a = int(input())
b = int(input())
operator = input()

# operation decition
if operator == "mod":
    if b == 0
        print("Division by 0!!!")
    else:
        ans = a%b
elif operator == "*":
    ans = a * b
elif operator == "/":
    if b == 0
        print("Division by 0!!!")
    else:
        ans = a%b

elif operator == "+":
    ans = a + b
elif operator == "-":
    ans = a - b
elif operator == "pow"
    ans = a ** b
elif operator == "div"
    ans = a // b
# print answer
print(ans)
"""

"""
# Farm
# define value
chicken, goat, pig, cow, sheep = 23, 678, 1296, 3848, 6769
# input user money
user_money = int(input("Your money: "))

# calculate amount of animal user can buy
for i in [sheep, cow, pig, goat, chicken]:
    check = user_money / i
    if check >= 1 and i == 6769:
        print(f"{check:.0f} sheep")
        break
    elif check >= 1 and i == 3848:
        print(f"{check:.0f} cow")
        break
    elif check >= 1 and i == 1296:
        print(f"{check:.0f} pig")
        break
    elif check >= 1 and i == 678:
        print(f"{check:.0f} goat")
        break
    elif check >= 1 and i == 23:
        print(f"{check:.0f} chicken")
        break
        """
"""
#day
# input offset
user_input_offset = int(input("Offset: "))
# define time
time = 10 + 30/60
# check user date
if time + user_input_offset > 24:
    print("Tuesday")
elif time + user_input_offset < 24:
    print("Monday")
    """

"""
def if_even(num):
    return num % 2 == 0
number = int(input("Number: "))
"""

"""
def leap_year(year):
    # check leap year
    if user_input_year % 4 == 0:
        if user_input_year % 100 == 0:
            if user_input_year % 400 == 0:
                return True
            else:
                return False
        else:
            return True

    else:
        return False


# input year
user_input_year = int(input("Year: "))

# call function leap_year
if leap_year(user_input_year) is True:
    print(f"{user_input_year} is leap year")
    """

"""
# check intersection
def interval_intersect(a, b, c, d):
    if a <= d and b >= c or (a >= b and d <= a):
        return True
    else:
        False


# print boolean
print(bool(interval_intersect(3, 5, 6, 9)))
"""

"""
# check digit 
def print_digit(user_num):
    if int(user_num) in range(0, 101):
        user_num = str(user_num)
        if int(user_num) < 10:
            print(f"The tens digit is 0 and the ones digits is {user_num[0]}")
        else:
            print(f"The tens digit is {user_num[0]} and the ones digits is {user_num[1]}")

    else:
        print("Error: Input is not a two-digit number.")
# input number and print it by fn 
user_num_input = input("Number: ")
print_digit(user_num_input)
"""

"""
# check that solution can be find
def smaller_root(a, b, c):
    check = b ** 2 - (4 * a * c)
    if check > 0:
        return True
    elif check < 0:
        return False
    elif check == 0:
        return 0

# input a b c
print("aX^2 + bX + c")
user_input_a = int(input("a:"))
user_input_b = int(input("b:"))
user_input_c = int(input("c:"))

# separate to 3 type
# first is have 2 solution
if smaller_root(user_input_a, user_input_b, user_input_c):
    x_1 = (- user_input_b - (smaller_root(user_input_a, user_input_b, user_input_c)) ** 1 / 2) / 2 * user_input_a
    x_2 = (- user_input_b + (smaller_root(user_input_a, user_input_b, user_input_c)) ** 1 / 2) / 2 * user_input_a
    print(f"x1 = {x_1}, x2 = {x_2}")
# second is solution cant be found
elif smaller_root(user_input_a, user_input_b, user_input_c) is False:
    print("Error: No real solutions")
# third is solution have only one solution
else:
    x_1 = (- user_input_b - (smaller_root(user_input_a, user_input_b, user_input_c)) ** 1 / 2) / 2 * user_input_a
    x_2 = (- user_input_b + (smaller_root(user_input_a, user_input_b, user_input_c)) ** 1 / 2) / 2 * user_input_a
    print(f"x = {x_1}")
    """

"""
# add odd number to num(str)
def there_is_odd(x, y, z):
    list_ = [x, y, z]
    num = ""
    for i in list_:
        if int(i) % 2 != 0:
            num += " " + str(i)

    return num

# input x y and z
x = input("x = ")
y = input("y = ")
z = input("z = ")

# check that x y or z is odd number and print it out
if there_is_odd(x, y, z) != "":
    print(f"There is an odd number whose value is{there_is_odd(x, y, z)}")
elif there_is_odd(x, y, z) == "":
    print("There is no odd number")
"""

"""
# add odd number to num(str)
def there_is_odd(w, x, y, z):
    list_ = [w, x, y, z]
    num = 0
    for i in list_:
        if int(i) % 2 != 0:
            print(f"This value is odd {i}")
        else:
            num += 1
    if num == 4:
        print("There is no odd number")


# input x y and z
first = input("1st = ")
second = input("2nd = ")
third = input("3rd = ")
forth = input("4th = ")

# check that x y or z is odd number and print it out
there_is_odd(first, second, third, forth)
"""


# check maximum number
def max_of_three(x, y, z):
    maxi = x

    if maxi < y:
        maxi = y
    if maxi < z:
        maxi = z
    return maxi


# input x y and z
first = input("1st = ")
second = input("2nd = ")
third = input("3rd = ")
# print answer
print(f"The max value is {max_of_three(first, second, third)}")
