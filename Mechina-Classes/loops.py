
# # Exercise 1: ---10 numbers---
# numbers = []
# for i in range(10):
#     x = int(input("Enter a number:"))
#     numbers.append(x)
# print(numbers)

# # Exercise 2: ---10 numbers square---
# numbers = []
# for i in range(10):
#     x = int(input("Enter a number:"))
#     numbers.append(x*x)
# print(numbers)

# # Exercise 3: ---20 numbers units number---
# numbers = []
# for i in range(20):
#     x = int(input("Enter a number:"))
#     numbers.append(x % 10)
# print(numbers)

# # Exercise 4: ---Double numbers---
# numbers = []
# for i in range(20):
#     x = int(input("Enter a number:"))
#     if x % 2 == 0:
#         numbers.append(x)
# print(numbers)

# # Exercise 5: ---Triple numbers sum---
# numbers = []
# for i in range(15):
#     x = int(input("Enter a number:"))
#     if 99 < x < 999:
#         first = int(x / 100)
#         second = int(x / 10) % 10
#         sum = first + second
#         numbers.append(sum)
# print(numbers)

# # Exercise 6: ---Under zero---
# numbers = []
# for i in range(30):
#     x = int(input("Enter a number:"))
#     if x < 0:
#         numbers.append(x)
# print(numbers)
# print(f"{len(numbers)} numbers are under zero")

# # Exercise 7: ---Is double number or not---
# numbers = []
# for i in range(12):
#     x = int(input("Enter a number:"))
#     if x % 2 == 0:
#         numbers.append(x)
#         print(f"The number {x} is double")
#     else:
#         print(f"The number {x} is NOT double")
#
# print(numbers)
# print(f"{len(numbers)} numbers are double")

# # Exercise 8: ---Average in class---
# numbers = []
# sum = 0
# for i in range(10):
#     x = int(input("Enter your grade:"))
#     numbers.append(x)
#     sum += x
# average = sum/len(numbers)
# print(f"The average is {average}")

# Easy way to do exercise 8 :)
# sum = 0
# for i in range(10):
#     x = int(input("Enter your grade:"))
#     sum += x
# average = sum/10
# print(f"The average is {int(average)}")

# # Exercise 9: ---Double the numbers without "*"---
# # def multiply(a, b):
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# total = 0
# counter = 0
# while counter < num2:
#     total += num1
#     counter += 1
# print(total)
# # return total
# # print(multiply(num1, num2))


# # Exercise 10: ---Closest to zero---
# import math
# plus = math.inf
# minus = math.inf * (-1)
# for i in range(10):
#     x = int(input("Enter a number:"))
#     if 0 < x < plus:
#         plus = x
#     elif 0 > x > minus:
#         minus = x
# print(f"{plus} is the plus closest to zero \n"
#       f"{minus} is the minus closest to zero")

# # Exercise 11: ---Factorial number---
# def factorial(a):
#     total = 1
#     while a != 0:
#         total *= a
#         a -= 1
#     return total
#
#
# num1 = int(input("Enter a number:"))
# print(factorial(num1))

# # Exercise 12: ---Range options---
# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter a number:"))
# if num1 > num2:
#     num1, num2 = num2, num1
# rangeNumbers = []
# dividingThreeAndSeven = []
# for x in range(num2 - num1):
#     if num1 < x < num2:
#         rangeNumbers.append(x)
#         if x % 3 == 0 and x % 7 == 0:
#             dividingThreeAndSeven.append(x)
# print(f"The Numbers are: \n {rangeNumbers} \n They were {len(rangeNumbers)} numbers.")
# print(f"The dividing by 3 and 7 are: \n {dividingThreeAndSeven} \n They were {len(dividingThreeAndSeven)} numbers.")

# # Exercise 13: ---Number dividers---
# num = int(input("Enter a number:"))
# dividers = []
# for x in range(1, num):
#     if num % x == 0:
#         dividers.append(x)
# print(f"The dividers are: \n {dividers}")

# # Exercise 14: ---Numbers 1 to 40---
# for x in range(1, 41):
#     print(x)

# # Exercise 15: ---Seven boom---
# sevenFamily = []
# for x in range(100):
#     units = x % 10
#     tens = int(x / 10)
#     if x % 7 == 0 or units == 7 or tens == 7:
#         sevenFamily.append(x)
# print(f"The sevens family is: \n {sevenFamily}")

# # שנה היא מעוברת אם בחלוקה ל-19 היא נותנת שארית 3, 6, 8, 11, 14, 17 או 0
# # Exercise 16: ---Leap year---
# year = int(input("Enter a year:"))
# if (year % 19 == 3 or year % 19 == 6 or year % 19 == 8 or
#         year % 19 == 11 or year % 19 == 14 or year % 19 == 17 or year % 19 == 0):
#     print(f"The year {year} is leap year")
# else:
#     print(f"The year {year} is NOT leap year")


# # Exercise 'Pass': ---Jumps by 0.1---
# nums = []
# for x in range(6):
#     if x == 5:
#         nums.append(x)
#         break
#     nums.append(int(x))
#     for y in range(1, 10):
#         nums.append(x+(y*0.1))
# print(f"The numbers are: \n {nums[0:10]} \n "
#       f"{nums[10:20]} \n {nums[20:30]} "
#       f"\n {nums[30:40]} \n {nums[40:51]}")
#
# # Exercise 'Pass': ---Number 6 in cube---
# import random
#
# counter = 1
# numbers = []
# while True:
#     num = random.choice([1, 2, 3, 4, 5, 6])
#     numbers.append(num)
#     if num == 6:
#         break
#     counter += 1
# print(f"The amount that took to get number 6 is: \033[1m {counter} cube drop \n "
#       f"Which they: {numbers} \033[0m <-this is bold :)")
