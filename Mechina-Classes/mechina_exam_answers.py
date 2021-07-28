# num = 0             # The grade
# count = 0           # counts how many grades are
# all_num = 0         # sum of all the grades
# count85 = 0         # counts how many grades are above 85
# lst = []            # Stores the grades in list
# while num != -1:    # -1 is the break point
#     num = int(input("Enter a number between 0 to 100:"))
#     if 0 <= num <= 100:     # Grade must be between 0 to 100 included
#         count += 1
#         all_num += num
#         lst.append(num)
#         if 85 < num <= 100:  # Asks how many grades are between 86 to 100 included
#             count85 += 1
#             if num >= 95:
#                 print("Excellent grade")
# lst.sort()                  # Sorts the grade storage
#
#
# print("The sum of the grades are: ", all_num/count)
# print("The number of grades above 85 are:", count85)
# print("The highest number in the class is: ", lst[-1])
#
#
# size = int(input("Enter the triangle size:"))
# for i in range(size):
#     print(" " * (size - i - 1) + '*' * (i + 1))
#     # number of spaces we need and number of * by the number we want



lst1 = []
num = int(input("Enter number of words: "))
for i in range(num):
    lst1.append(input("Enter word: "))
final = [0] * num

for i in range(len(lst1)):
    count = lst1[i].count('a') + lst1[i].count('e') + lst1[i].count('i') + lst1[i].count('o') + lst1[i].count('u')
    final.insert(count, lst1[i])

final2 = []
for i in final:
    if isinstance(i, str):
        final2.append(i)
print(lst1)
print(final2[::-1])



# def Replace(st, search, rep):
#     if search in st:
#         return st.replace(search, rep)
#     else:
#         return -1
#
# st = "mississipi"
# search = "iss"
# rep = 'ita'
# print(Replace(st,search,rep))

# word = 'Itanjmar'
# file = "C:\\Users\Student\Desktop\itamar.txt"
# c = 0
# word = word.lower()
# with open(file) as text:
#     for line in text:
#         line = line.strip()
#         if line.lower() == word:
#             c += 1
#     if c == 0:
#         print("The word was not found")
#     else:
#         print(c)
