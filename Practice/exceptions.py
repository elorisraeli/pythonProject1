# while True:
#     try:
#         x = int(input("Please enter a number: "))
#         break
#     except ValueError:
#         print("Oops!  That was no valid number.  Try again...")

x = int(input("Enter a number:"))
y = int(input("Enter divider number:"))
try:
    divide = x / y
    print(divide)
except:
    print("You cant divide by zero")
