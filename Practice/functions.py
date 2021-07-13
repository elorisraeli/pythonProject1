# Functions which doing basic things:

# Example 1: Reverse string
def end_to_start(string):
    return string[::-1]


print(end_to_start("sdfkjghsdjkfgheoir"))


# Example 2: Calculator
def math_calc(num1, operator, num2):
    if num1 == int(num1) and num2 == int(num2):
        if operator == '+':
            return num1 + num2
        if operator == '-':
            return num1 - num2
        if operator == '*':
            return num1 * num2
        if operator == '/':
            return num1 / num2
        else:
            return "Invalid operator"
    else:
        return "Only integer numbers."


print(math_calc(4, "*", 5))


# Example 3: Sum of list
def sum_list(lst):
    total = 0
    for i in lst:
        # check if the index in the list is an integer number
        if i == int(i):
            total += i
    return total


print(sum_list([1, 3, 100, 7]))
