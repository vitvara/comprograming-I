water = 10
milk = 540
coffee = 120
cups = 9
money = 550

def resource_remain(w, m, coff, cup):
    global water, milk, coffee, cups
    remaining_list = [water, milk ,coffee, cup]
    needed_list = [w, m, coff, cup]
    name_resource = ["water", "milk", "coffee", "cup"]

    for i in range(len(resource_list)):
        print(resource_list[i])
        print(f"Please fill {name_resource[i]} to {resource_list[i] - remaining_list[i]} ml")
        if resource_list[i] > remaining_list[i]:
            if remaining_list[i] in [w, m]:
                print(f"Please fill {name_resource[i]} to {resource_list[i] - remaining_list[i]} ml")
            elif remaining_list[i] in [coff]:
                print(f"Please fill coffee beans to {resource_list[i] - remaining_list[i]}")
            else:
                print(f"Please fill up to {resource_list[i] - remaining_list[i]} cups")

print("I CAN'T MAKE CUP OF COFFEE")
resource_remain(water, milk, coffee, cups)