# define fn fib
def fib(n):
    """
    this funtion stack fib num and print out into ladder
    """
    count = 0
    n1 = 0
    n2 = 1
    string_num = "1 "
    print(n2)
    # fibnocii loop untill it's repeat the same amount as parameter input
    while count <= n:
        fib_n = n1 + n2
        count += 1
        n1 = n2
        n2 = fib_n
        string_num += str(fib_n) + " "
        print(string_num)

def diamond(a): 
    """
    function that make stupid diamond shape loop for something
    """
    stri = " "

    for n in range(1, a * 2):
        if n % 2 == 1:
            #top diamond      
            for i in range(0, n):
                stri += " " * (n // 2 - i)
                stri += "*" * (2 * (i + 1))
                print(stri)
                stri = " "

                if n // 2 - i == 0:
                    break
            #bot diamond  
            for i in range(0, n//2 + 1):
                stri += " " * (i)
                stri += "*" * (2*(n//2 - i + 1))
                print(stri)
                stri = " "

            print("")
        
def hailstone(n):
    """
    function print hailstone sequence  
    """
    hailstone_print = ""
    # loop hailstone
    for i in range(1, n + 1):
        hailstone_print += str(i) + " "

        # check that number is not equal to 1
        while i  != 1:
            # check even number
            if i % 2 == 0:
                i = i // 2
            
                hailstone_print += str(i) + " "
            # check odd number
            else:
                i = (3 * i) + 1
            
                hailstone_print += str(i) + " "

        print(hailstone_print)
        hailstone_print = ""

def arith_sum(n):
    """
    this function make a loop of arith sum
    """
    # define valuable
    answer_str = ""
    # loop all number
    for i in range(1, n+1):
        answer = 0
        # loop number
        for j in range(1, i+1):
            answer_str += str(j) + " + "
            answer += j
            
        print(f"{answer_str} = {answer}")
        # set answer_str to ""
        answer_str = ""
    

diamond(3)
arith_sum(10)