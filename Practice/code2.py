print("Get numbers from string + print string length")
# get string from user
s = input("input a line:")
# string length
letter = len(s)
i = 0
number_array = []
# start the loop
while i < letter:
    num = ''
    # getting char from the string in the "i" location in the array (s array)
    symbol = s[i]
    # if the char is a digit so start a loop, else just dont get in the loop
    while symbol.isdigit():
        # num = plus the digit
        num += symbol
        # (up 5 code lines are) to don't get index out of range
        i += 1
        if i < letter:
            symbol = s[i]
        else:
            break
    if num != '':
        # add the number to the array
        number_array.append(num)
    i += 1
print(f"The length of all this is: {len(s)}, \n numbers found in the string are: {number_array}")
