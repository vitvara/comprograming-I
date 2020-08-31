# ++ -+ -- +-
print("Input a point (x,y):")
x = float(input("x = ? "))
y = float(input("y = ? "))

if x > 0 and y > 0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 1.")
elif x < 0 and y > 0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 2.")
elif x < 0 and y < 0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 3.")
elif x > 0 and y < 0:
    print(f"The point ({x:.2f},{y:.2f}) is in quadrant 4.")
elif x == 0 and y == 0:
    print("The point (0.00,0.00) is at the origin.")
elif x == 0:
    print(f"The point (0.00,{y:2.f}) is on the y-axis.")
elif y == 0:
    print(f"The point ({x:.2f},0.00) is on the x-axis.")

