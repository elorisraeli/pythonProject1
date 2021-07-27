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
