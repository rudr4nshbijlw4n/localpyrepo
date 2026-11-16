print('''This is First Python project
The code will be simple Arithmetic Operations''')
num1 = int(input("Enter a Number: "))
num2 = int(input("Enter another Number: "))
list_of_operations = ["Addition", "Subtraction", "Multiplication", "Division", "Remainder"]
for i, op in enumerate(list_of_operations):
    print(f"{i+1}. {op}")
print()
choice = int(input("Your Choice : "))
try:
    if choice > 5 or choice < 1:
        print("[ERROR] - Invalid choice!")
    else:
        if choice == 1:
            print(f"Sum of {num1} + {num2} = {num1 + num2}")
            print()

        elif choice == 2:
            print(f"Difference of {num1} - {num2} = {num1 - num2}")
            print()

        elif choice == 3:
            print(f"Product of {num1} * {num2} = {num1 * num2}")
            print()

        elif choice == 4:
            print(f"Division of {num1} / {num2} = {num1 / num2}")
            print()

        elif choice == 5:
            print(f"Remainder of {num1} % {num2} = {num1 % num2}")
            print()
except TypeError:
    print("[ERROR] - Ivalid Input!")