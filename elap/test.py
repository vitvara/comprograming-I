def diamond(n):
    n = n+1
    x = " "
    for i in range(1, n+1):
        
        x += " " * (n-i)
        x += "**" * i

        print(x)
        x = " "
    for i in range(1, n+1):
        
        x += " " * (i -1)
        x += "**" * (n + 1 -i)

        print(x)
        x = " "

print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")



