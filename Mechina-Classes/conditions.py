# # Exercise 1: ---Age Checking---
# age = int(input("Enter your age:"))
# if age == 18:
#     print("Congratulations")
# elif age < 18:
#     print("You are so young")
# else:
#     print("We love old people")

# # Exercise 2: ---Positive number---
# number = int(input("Enter an integer number:"))
# if number < 0:
#     print(0 - number)
# else:
#     print(number)

# # Exercise 3: ---Person pension---
# age = int(input("Enter your age:"))
# if age == 65:
#     print("You start pension now")
# elif age < 65:
#     years_left = 65-age
#     print(f"You have {years_left} years to pension")
# else:
#     print("You are in pension")

# # Exercise 4: ---Payment and chatty---
# phoneCalls = int(input("Enter number of phone calls:"))
# pricePerCall = int(input("Enter price per call:"))
# payment = phoneCalls * pricePerCall
# if phoneCalls > 500:
#     print(f"Payment: {payment}, you are chatty")
# else:
#     print(f"Payment: {payment}")

# # Exercise 5": ---Is 6 inside?---
# positiveNumber = int(input("Enter a double digit number:"))
# first = int(positiveNumber / 10)
# second = positiveNumber % 10
# if first == 6 or second == 6:
#     print("Number 6 is in the number")
# else:
#     print("Number 6 is NOT in the number")

# # Exercise 6: ---Dividing number---
# number1 = int(input("Enter the first number:"))
# number2 = int(input("Enter the second number:"))
# if (number1 % number2) == 0:
#     print("Number 2 is a divider of number 1")
# else:
#     print("Number 2 is NOT a divider of number 1")

# # Exercise 7: ---Biggest number---
# number1 = int(input("Enter number 1:"))
# number2 = int(input("Enter number 2:"))
# number3 = int(input("Enter number 3:"))
# biggest = 0
# if number1 > number2:
#     biggest = number1
#     if number1 < number3:
#         biggest = number3
# elif number2 > number3:
#     biggest = number2
# else:
#     biggest = number3
# print(f"Number {biggest} is the biggest")

# # Exercise 8: ---Phone using---
# beats = int(input("Enter number of beats in phone:"))
# vat = 1.17
# regularUsesFee = 75
# if beats <= 100:
#     payment = (beats * 0.4)*vat + regularUsesFee
#     print(f"You need to pay {payment} shekels")
# else:
#     payment = (beats * 0.3)*vat + regularUsesFee
#     print(f"You need to pay {payment} shekels")

# # Exercise 9: ---Sort by ascending order---
# number1 = int(input("Enter number 1:"))
# number2 = int(input("Enter number 2:"))
# number3 = int(input("Enter number 3:"))
# if number1 > number2 > number3:
#     print("The numbers are sorted in ascending order")
# elif number3 > number2 > number1:
#     print("The numbers are sorted in ascending order")
# else:
#     print("The numbers are NOT sorted in ascending order")

# # Exercise 10: ---Invoice series---
# number1 = int(input("Enter number 1:"))
# number2 = int(input("Enter number 2:"))
# number3 = int(input("Enter number 3:"))
# if (number3 - number2) == (number2 - number1):
#     print("The 3 numbers are invoice series")
# else:
#     print("The 3 numbers are NOT invoice series")

# # Exercise 11: ---Pass or not---
# number1 = int(input("Enter grade of 'Introduction to programming':"))
# number2 = int(input("Enter grade of 'linear algebra':"))
# number3 = int(input("Enter grade of 'Computer Architecture':"))
# if (number1 >= 80 and number2 >= 80) or (number2 >= 80 and number3 >= 80) or (number3 >= 80 and number1 >= 80):
#     print("You are pass to year 2 of Computer Science")
# else:
#     print("You are NOT pass to year 2 of Computer Science")

# # Exercise 12: ---Triangle or not---
# number1 = int(input("Enter first side of the triangle:"))
# number2 = int(input("Enter second side of the triangle:"))
# number3 = int(input("Enter third side of the triangle:"))
# if ((number1 + number2) > number3) and ((number1 + number3) > number2) and ((number2 + number3) > number1):
#     print("This could be a triangle")
# else:
#     print("This could NOT be a triangle")

# # Exercise 13: ---While True Fibonacci---
# num1 = 0
# num2 = 1
# counter = 2
# print(f"Number {0} is: {num1}")
# print(f"Number {1} is: {num2}")
# while True:
#     num3 = num2 + num1
#     if num3 > 10000:
#         break
#     print(f"Number {counter} is: {num3}")
#     num1 = num2
#     num2 = num3
#     counter += 1
# print("This is all fibonacci numbers under 10000")
