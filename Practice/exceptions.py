while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")

x = int(input("Enter a number:"))
y = int(input("Enter divider number:"))
try:
    divide = x / y
    print(divide)
except:
    print("You cant divide by zero")

sentence = input("Enter some words:")
anything = int(input("Enter a number:"))
try:
    sentence += anything
except:
    print("Just kiddin' this is an exception to write the way i did :)")
    print("Python can not add int to string with '+=' you can use '{}' or '' :)")
