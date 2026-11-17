print("This project will contain code to print '*' Pattern")
print()

rows = int(input("Enter number of Rows: "))

print("Pattern 1")
for row in range(1, rows + 1):
    for cols in range(1, row + 1):
        print("*", end = ' ')
    print()
print()

print("Pattern 2")

for row in range(rows, 0, -1):
    for cols in range(1, row + 1):
        print("*", end = ' ')
    print()
print()

print("Pattern 3")
for row in range(0, rows):
    for cols in range(0, 5 - row):
        print(" ", end = " ")
    for k in range(0, row + 1):
        print("*", end = ' ')
    print()
print()

print("Pattern 4")
for row in range(rows, 0, -1):
    for cols in range(5 - row, 0, -1):
        print(" ", end = ' ')
    for k in range(row, 0, -1):
        print("*", end = ' ')
    print()
print()

print("Pattern 5")
for row in range(1, rows + 1):
    for spaces in range(0, 5 - row):
        print(" ", end = ' ')
    for astrik in range(0, 2 * row - 1):
        print("*", end = ' ')
    print()
print()

print("Pattern 6")
for row in range(rows, 0, -1):
    for spaces in range(5 - row, 0, -1):
        print(" ", end = ' ')
    for astrik in range(2 * row - 1, 0, -1):
        print("*", end = ' ')
    print()
print()

print('DONE!!')