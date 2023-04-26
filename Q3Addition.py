import random
num1 = random.randint(1, 100)
num2 = random.randint(1, 100)
while True:
    try:
        answer = float(input(f"What is {num1} + {num2}? "))
        if answer != num1 + num2:
            print("😥 wrong!!")
            continue
        break
    except ValueError:
        print("Invalid input! Please enter numbers only.")

print("You are correct 👍!")
