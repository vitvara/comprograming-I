def diamond(n):
    x = " "
    if n % 2 == 1:
        for i in range(0, n):
            x += " " * (n // 2 - i)
            x += "*" * (2 * (i + 1))
            print(x)
    else:
        for i in range(0, n//2+1):
            x += " " * (i)
            x += "*" * (2 * (n//2 - i + 1))
            print(x)

print("diamond(n) result:")
for i in range(0, 8):
    diamond(i)
    print("")
