a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
import math
def my_sqrt(a):
    x = int(input("Enter num: "))
    while True:
        y = (x + a/x) / 2
        if y == x:
         break
        x = y

def test_square_root():
    print(f"a  mysqrt(a)  math.sqrt(a)  diff")
    print(f"-  ---------  ------------  ----")
    for i in a:
        print(f"{i}   {round(my_root(i), 11):<14}{round(math.sqrt(i), 11):<14}{math.sqrt(i) - my_root(i)}")

print(test_square_root())

