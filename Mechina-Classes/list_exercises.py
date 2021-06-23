# # Exercise 1: ---Print with jumps of 2---
# stam = [11, 'aaaa', 36.5, True, ['a', 'b', 'c']]
# print(stam[::2])
#
#
# # Exercise 2: ---Function to sum lists--- (Liron's answer)
# def summer(lst, lst2=[]):
#     if lst2 != []:
#         return lst + lst2
#     res = 0
#     res2 = ''
#     flag = False
#     for i in lst:
#         if type(i) == str:
#             res2 += i
#             flag = True
#         else:
#             res += 1
#     if flag:
#         return res2
#     else:
#         return res
#
#
# print(summer([10, 11, 12, 0.75]))
# print(summer([True, False, True, True]))
# print(summer(['aa', 'bb', 'cc', 'dd']))
# print(summer([1, 2, 3, 'a'], [4, 'b', 'c', 'd']))

# # Exercise 3: ---Sort list by last char of the elements---
# animals = ['cat', 'zebra', 'dog', 'giraffe']
#
#
# def last(lst1):
#     return lst1[::-1]
#
#
# lst = sorted(animals, key=last)
# print(lst)


# # # After tuple explanation
# # Exercise 1: ---Create List with jumps of 2---
# lst = []
# for i in range(2, 11):
#     if i % 2 == 0:
#         lst.append(i)
# print(lst)

# # Exercise 2: ---Delete empty elements from list---
# lst = ["Emma", "Jon", "", "Kelly", None, "Eric", ""]
# for i in lst:
#     if type(i) != str or i == "":
#         lst.remove(i)
# print(lst)

# # Exercise 3: ---Get list from user---
# string = input("Enter sentence:")
# string = string.split(" ")
# print(string)

# # Exercise 4: ---List of chars and their count in string---
# line = input("Enter a line:")
# lst = []
# for char in line:
#     if char in lst:
#         pass
#     else:
#         lst.append(char)
#         lst.append(line.count(char))
# print(lst)

# Exercise 5: ---Under 18 only first name, else last name too---
import datetime

year_now = datetime.datetime.now().year
year_born = int(input("Enter the year you were born:"))
# ^^^ also could just ask for age :) ^^^
# like that -> age = input("Enter your age:")
first = input("Enter your first name:")
age = year_now - year_born
if age < 18:
    print(f"Thank you {first} and goodbye")
else:
    last = input("Enter your last name:")
    print(f"Thank you for using {first} {last}, have a great day")
