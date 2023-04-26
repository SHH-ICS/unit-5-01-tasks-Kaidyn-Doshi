
import random

while True:
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        if num1 > num2:
            print("Invalid input! The first number should be smaller than or equal to the second number.")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.")

random_num = random.uniform(num1, num2)

print(f"A random number between {num1} and {num2} is {random_num:.1f}")
