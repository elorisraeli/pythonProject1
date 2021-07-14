# # Exercise 1: ---Run until 'q', sum all numbers---
# total = 0
# while True:
#     num = input("Enter numbers, if you done enter 'q':")
#     if num.isdigit():
#         int_num = int(num)
#         total += int_num
#     elif num == "q":
#         print(f"Sum is: {total}")
#         break


# # Exercise 2: ---Get list, number. clean list, don't have number dividing by number---
# def clean_list(lst, divisor):
#     for i in lst:
#         if i % divisor == 0:
#             lst.remove(i)
#     return lst


# print(clean_list([1, 2, 3, 4, 5, 6, 7, 8, 9], 3))

# # Exercise 3: ---Check if string is same when reversed---
# string = input("Enter something to check:")
# if string == string[::-1]:
#     print(f"The string '{string}' is palindrome")
# else:
#     print("NOT a palindrome")


# # Exercise 4: ---Lotto game, guess 3 different numbers between 0-9 to win---
# import random
# guess1 = int(input("Guess number 1:"))
# guess2 = int(input("Guess another number:"))
# guess3 = int(input("Guess another number:"))
# win_numbers = []
# # get the random numbers into the list
# while True:
#     number = random.randint(0, 9)
#     if number not in win_numbers:
#         win_numbers.append(number)
#     else:
#         pass
#     if len(win_numbers) == 3:
#         break
# # check if guesses in the list of random numbers
# if guess1 in win_numbers and guess2 in win_numbers and guess3 in win_numbers:
#     print(f"You Win \n Lotto winner numbers are: {win_numbers}")
# else:
#     print(f"You Lose \n Lotto winner numbers are: {win_numbers}")


# # Exercise 5: ---Sum numbers from txt file---
# total = 0
# with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/numbers.txt', 'r') as file_nums:
#     for line in file_nums:
#         nums_list = line.split(" ")
#         for num in nums_list:
#             if num.isdigit():
#                 total += int(num)
#         nums_list.clear()
# print(f"The sum of all the numbers in the file is: {total}")


# # Exercise 6: ---Count each number in list---
# # option 1: -save in list-
# def count_each(lst):
#     new_list = []
#     # check if the object we got it list
#     if isinstance(lst, list):
#         for num in lst:
#             # add the count of the number to new list
#             new_list.append(lst.count(num))
#             # remove all the number locations from original list
#             for i in lst:
#                 if i == num:
#                     lst.remove(i)
#     return new_list
#
#
# print(count_each([0, 5, 5, 4, 3, 2, 3, 5, 7, 8, 2, 2, 9]))
#
#
# # option 2: -save in dictionary-
# def count_each2(lst):
#     count_dict = {}
#     # check if the object we got it list
#     if isinstance(lst, list):
#         for num in lst:
#             # add the count of the number to new list
#             count_dict[num] = lst.count(num)
#             # remove all the number locations from original list
#             for i in lst:
#                 if i == num:
#                     lst.remove(i)
#     return count_dict
#
#
# print(count_each2([0, 5, 5, 4, 3, 2, 3, 5, 7, 8, 2, 2, 9]))


# Exercise 7: ---Check valid list with only int type---
def check_list(lst):
    if isinstance(lst, list):
        for i in lst:
            try:
                if i >= 0:
                    print(i)
                else:
                    print("This number is out of range (under zero)")
            except ValueError:
                print("This is ValueError type")
            except TypeError:
                print("This is TypeError type, index in list is not an int..")


check_list([3, 4, 6, 7, 8, ":rg", 453, "fger", -35, -76])
