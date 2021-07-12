# Functions which doing basic things:

# Example 1:
def end_to_start(string):
    return string[::-1]


print(end_to_start("sdfkjghsdjkfgheoir"))


# Example 2:
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
