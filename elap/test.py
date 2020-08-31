user_input = float(input("Enter a real number: "))

if user_input < 15:
    print(f"f({user_input:.3f}) = {2 * user_input + 10:.3f}")

elif 15 < user_input < 35:
    print(f"f({user_input:.3f}) = {3 * (user_input ** 2):.3f}")

else:
    print(f"f({user_input:.3f}) = {2 * (user_input ** 3) - 5:.3f}")
