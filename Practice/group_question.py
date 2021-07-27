# bring the string library
import string


def histogram(sentence):
    # check if string only with small chars and spaces
    flag = True
    for char in sentence:
        if char.islower() or char == " ":
            flag = True
        else:
            flag = False
    # if is really as we want -> lets start to print the histogram
    lst = [0] * 26
    if flag:
        for j in range(0, 25):
            for i in sentence:
                # lowercase from a to z in location j
                if string.ascii_lowercase[j] == i:
                    lst[j] += 1
    print(string.ascii_lowercase)
    for j in range(max(lst)):
        for i in range(len(lst)):
            if lst[i] > 0:
                print('*', end='')
                lst[i] -= 1
            else:
                print(' ', end='')
        print()


histogram("aba ima")

histogram("asd fvadf sdf adf")


# if flag:
#         dictionary_chars = {}
#         # run of all chars in string
#         for character in sentence:
#             # not including the spaces and check if char not already in dictionary
#             if (not character == " ") and (not character in dictionary_chars.keys()):
#                 # add to dictionary the char and how much times it appear in string
#                 dictionary_chars[character] = sentence.count(character)
#                 # clean from string all the appearances of the char
#                 for i in sentence:
#                     if i == character:
#                         sentence = sentence.replace(character, '')
#         print(dictionary_chars)
#         # create new dictionary to print nicely
#         new_dictionary = {}
#         # get the max value from the values in first dictionary
#         max_values = max(dictionary_chars.values())
#         while max_values != 0:
#             abc_lowers = string.ascii_lowercase
#             # for lower
#             # new_dictionary['sentence_*'] =
#         # print(string.ascii_lowercase)
#
#
# histogram("asd fvadf sdf adf")
