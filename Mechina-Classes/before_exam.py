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


# Exercise 5: ---Sum numbers from txt file---
total = 0
with open(r'C:\Users\Elor Israeli\Desktop\מבוא למחשבים\homework/numbers.txt', 'r') as file_nums:
    for line in file_nums:
        nums_list = line.split(" ")
        for num in nums_list:
            if num.isdigit():
                total += int(num)
        nums_list.clear()
print(f"The sum of all the numbers in the file is: {total}")

