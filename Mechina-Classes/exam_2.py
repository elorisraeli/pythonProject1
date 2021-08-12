# # Exercise 1: ---Grades list---
# grades = []
# print("if you done enter -1")
# while True:
#     grade = int(input("Enter a integer grade:"))
#     if grade == -1:
#         break
#     else:
#         grades.append(grade)
#
# # Exercise 1.1: -Average-
# total = 0
# for i in grades:
#     total += i
# average = total/len(grades)
# print(f"The average is: {average}")
#
# # Exercise 1.2: -Minimum grade-
# minimum = min(grades)
# print(f"The minimum is: {minimum}")

# # Exercise 2: ---Reverse string---
# sentence = input("Enter a sentence:")
# words = sentence.split(" ")
# new_sentence = ""
# for word in words:
#     new_sentence = new_sentence + word[::-1] + " "
# print(new_sentence)

# # Exercise 3: ---Count alphabet chars in string---
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

# # Exercise 4: ---Count number digits---
# num = int(input("Enter a number:"))
# num_length = len(str(num))
# print(f"The number have {num_length} digits")

# # Exercise 5: ---Replace from file---
# def replace_in_file(file_name, search_word, replace_word):
#     flag = False
#     with open(file_name, 'w') as my_file:
#         for line in my_file:
#             if search_word in line:
#                 line = line.replace(search_word, replace_word)
#                 flag = True
#     if not flag:
#         print("The word was not found")
#
#
# f_name = r"C:\Users\Elor Israeli\Desktop/myfile.txt"
# s_word = "would"
# r_word = "blablablaaaaaa"
# replace_in_file(f_name, s_word, r_word)
