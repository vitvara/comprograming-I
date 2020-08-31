check = 0
size_1 = float(input("Enter 1st line's length: "))
size_2 =  float(input("Enter 2nd line's length: "))
size_3 = float(input("Enter 3rd line's length: "))

if size_1**2 == size_3**2 + size_2 **2:
    print("It's a right triangle.")
elif size_2**2 == size_1**2 + size_3 **2:
    print("It's a right triangle.")
elif size_3**2 == size_1**2 + size_2 **2:
    print("It's a right triangle.")

elif size_1 + size_2 <= size_3:
    print("It's not a triangle.")
                                                                                                                                         
elif size_1 + size_3 <= size_2:
    print("It's not a triangle.")
       
elif size_3 + size_2 <= size_1:
    print("It's not a triangle.")
else:
    print("It's a triangle but not a right triangle.")
    
