# Exercise 1: ---Number length of asterisks---
def asterisk(num):
    string = ''
    for i in range(num):
        string += '*'
    return string


print(asterisk(10))


# Exercise 2: ---Sum of 2 numbers---
def multiply(x, y):
    return x * y


print(multiply(5, 6))


# Exercise 3: ---Rectangle of asterisks---
def rectangle(width, height):
    line = ''
    for i in range(width):
        line += '*'
    rectangle = ''
    for x in range(height):
        rectangle += f"{line}\n"
    return rectangle


print(rectangle(10, 4))


# Exercise 4: ---Rectangle of any sign---
def rectangle(width, height, sign):
    line = ''
    for i in range(width):
        line += f'{sign}'
    rectangle = ''
    for x in range(height):
        rectangle += f"{line}\n"
    return rectangle


print(rectangle(10, 4, '#'))


# Exercise 5: ---Power of number with another---
def power(x, y):
    return x ** y


print(power(5, 6))


# Exercise 6: ---Upside down a number---
def upside_down(num):
    a = str(num)
    b = a[::-1]
    return int(b)


print(upside_down(167))


# Exercise 7: ---Char in string---
def find(char, string):
    counter = string.count(char)
    if counter == 0:
        return -1
    else:
        return counter


print(find('a', "abanibi obohebev obotabach"))


# Exercise 8: ---Factorial of number---
def factorial(num):
    sum = 1
    for i in range(num):
        sum = sum * num
        num -= 1
    return sum


print(factorial(5))


# Exercise 9: ---Add beep to string---
def beep(string):
    return f"{string} beep"


print(beep("what does the fox say?"))


# Exercise 10: ---Multiply under zero?---
def mul_2nums(x, y):
    if (x * y) < 0:
        return 0
    else:
        return x * y


print(mul_2nums(9, -20))


# Exercise 11: ---Number of digits in number---
def digits(num):
    return len(str(num))


print(digits(12345678))
