# # Exercise 1: ---Print length---
# line = input("Enter your username:\n")
# print(f"Username length is: {len(line)}")

# # Exercise 2: ---Big letters with my own start---
# line = input("Enter a line:\n")

# # Option 1: -With built method-
# line = "programmer start " + line.lower()
# print(f"The string now is: {line}")

# # Option 2: -Without built method-
# # (looking for ascii numbers to use it later)
# import string
#
# for i in string.ascii_lowercase:
#     print(f"Char {i} is {ord(i)}")  # (lowercase are between 97-122 (a=97, b=98...))
# for x in string.ascii_uppercase:
#     print(f"Char {x} is {ord(x)}")  # (uppercase are between 65-90 (A=65, B=66...))
# # (Found from here ^^^ : UPPERCASE-lowercase=32)

# # (Now lets use it)
# for i in line:
#     if 64 < ord(i) < 91:  # (Upper case)
#         chr(ord(i) + 32)  # (Translate to char (lowercase) and add the value i found before(with ascii))
# print(f"The string now is: {line}")

# # Exercise 3: ---Each char counter---
# line = input("Enter a line:")
# for i in line:
#     if line.count(i) != 0:
#         print(f"Char {i}, {line.count(i)} times")
#         for char in line:
#             if char == i:
#                 line = line.replace(char, '')

# # Exercise 4: ---Count the zero---
# num = input("Enter a number:")
# counter = 0
# for i in num:
#     if i == "0":
#         counter += 1
# print(f"This number has {counter} times zero")

# # Exercise 5: ---Chars counter---
# line = input("Enter a line:")
# counter = 0
# for i in line:
#     # (i != ' ') ---> don't count the spaces
#     if i in line and i != ' ':
#         counter += 1
#         for char in line:
#             if char == i:
#                 line = line.replace(char, '')
# print(f"There are {counter} alphabetic chars")

# # Exercise 6: ---"Plant" string---
# line = input("Enter a sentence:")
# sub_string = input("Enter string to connect first sentence:")
# num = int(input("Enter the spot you want to enter second string:"))
# new_line = line[:num] + sub_string + line[num:]
# print(new_line)

# # Exercise 7: ---Upside down the line---
# line = input("Enter a sentence:")
# # reverse the line
# reverse = line[::-1]
# # split the words to list
# words = reverse.split()
# # reverse the list of words
# words = words[::-1]
# # join the words and add space between
# new_line = " ".join(words)
# print(new_line)

# # Exercise 8: ---Big letter after space---
# line = input("Enter a sentence:")
# # replace first letter to big character
# line = line.replace(line[0], chr(ord(line[0]) - 32))
# for i in range(len(line)):
#     if line[i] == ' ':
#         # each character after space, will replace to big character (uppercase)
#         line = line.replace((line[i + 1]), chr(ord(line[i + 1]) - 32))
# print(line)
