list_ = [1, 2, 3, 4]
def print_list(list_):
    for i in list_:
        print(i)

def read_list():
    xlist = []
    for i in range(n):
        xlist.append(float(input(f"Enter value{i+1}: ")))
    return xlist


n = int(input("Enter n: "))
print("Area(a) or Perimeter(P)")
print("side1")
side1 = read_list()
print("side2")
side2 = read_list()
for i in range(len(side1)):
    print(float(side1[i]) * float(side2[i]))



     
