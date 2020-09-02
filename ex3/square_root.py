import math

# define fn root
def my_root(a):
    """
    Root fn that have equation = (x + a / x) / 2
    This fn loop untill it got a right answer
    """
    # define x
    x = 2
    # make loop that loop untill it's has a right answer
    while True:
        y = (x + a / x) / 2
        # when answer is repeat twice return answer
        if x == y:
            return y
        x = y

# define fn print        
def print_result():
    """
    print table of myroot compare to math.sqrt
    """
    print(f"a   mysqrt(a)     math.sqrt(a)  diff")
    print(f"-   ---------     ------------  ----")
    # make for loop that loop 9 time
    for i in range (1, 10):     
        # print all answer
        print(f"{i}   {round(my_root(i), 11):<14}{round(math.sqrt(i), 11):<14}{math.sqrt(i) - my_root(i)}")


print_result()