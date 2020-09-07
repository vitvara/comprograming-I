def fib(n):
    """This function prints a Fibonacci sequence up to the nth Fibonacci
    """
    count = 0
    n1 = 0
    n2 = 1
    string_num = ""
    while count <= n:
        fib_n = n1 + n2
        count += 1
        n1 = n2
        n2 = fib_n
        string_num += str(fib_n) + " "
    print(string_num)

# fill me in


print("fib(n) result:")
n = 0
while n < 10:
    fib(n)
    n += 1


def diamond(n):
    """This function prints a diamond shape of size n as shown in loop_exercise_result.txt
    """
    stri = " "
    # top diamond
    

        for i in range(0, n):
            stri += " " * (n // 2 - i)
            stri += "*" * (2 * (i + 1))
            print(stri)
            stri = " "

            if n // 2 - i == 0:
                break
        # bot diamond
        for i in range(0, n//2 + 1):
            stri += " " * (i)
            stri += "*" * (2*(n//2 - i + 1))
            print(stri)
            stri = " "

        print("")


# fill me in

print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")


def hailstone(n):
    """This function prints a hailstone sequence whose details can be found in this link:
        http://mathworld.wolfram.com/CollatzProblem.html
    """

    hailstone_print = ""
    # loop hailstone

    hailstone_print += str(n) + " "

    # check that number is not equal to 1
    while n != 1:
        # check even number
        if n % 2 == 0:
            n = n // 2

            hailstone_print += str(n) + " "
        # check odd number
        else:
            n = (3 * n) + 1

            hailstone_print += str(n) + " "

    print(hailstone_print)
    hailstone_print = ""
# fill me in


print("hailstone(n) result:")
for i in range(1, 8):
    hailstone(i)
    print("")


def arith_sum(n):
    """This function prints the arithmetic sequence starting from 1 to nth together with its sum
    """
    answer = 1
    answer_str = "1"

    
    # set answer_str to ""
    for i in range(2, n):

        answer_str += " + " + str(i)
        answer += n
    print(f"{answer_str} = {answer}")
# fill me in

print("arith_sum(n) result:")
for i in range(1, 10):
    arith_sum(i)
    print("") 


