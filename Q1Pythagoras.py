import math

while True:
    try:
        a = float(input("Enter the length of side a: "))
        b = float(input("Enter the length of side b: "))
        if a <= 0 or b <= 0:
            print("Invalid input! Please enter a positive number only.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter a positive number only.")

c = math.sqrt(a**2 + b**2)

print(f"The length of the hypotenuse is {c:.2f} units")
