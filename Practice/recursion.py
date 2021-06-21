def recursion(x):
    if x > 0:
        result = x + recursion(x - 1)
        print("num is:", x, "\nthe result is:", result)
    else:
        result = 0
    return result


print("Result is: ")
recursion(10)