list_ = [1, 2, 3, 4]
def print_list(list_):
    for i in list_:
        print(i)

def read_list():
    n = int(input("Enter n: "))
    xlist = []
    for i in range(n):
        xlist.append(float(input(f"Enter value{i+1}: ")))
    return xlist

print_list(read_list())

     
