# Find any number in fibonacci:
number_to_find = int(input("Enter a number to find in fibonacci:"))


def fibonacci():
    total = 1
    num1 = 0
    num2 = 1
    counter = 0
    while str(total).find(str(number_to_find)) == -1:
        print(f"{counter}: {total}")
        counter += 1
        total = num1 + num2
        num1, num2 = num2, total
    print(f"{counter}: {total}")
    index = str(total).find(str(number_to_find))
    print(f"The number is in index: {index}")
    print(f"Last index is: {len(str(total))}")
    # Let me know where is the number I look for, by bold and arrows
    print(f"{str(total)[0:index]} --->>> \033[1m {str(total)[index:index+len(str(number_to_find))]} \033[0m <<<---"
          f" {str(total)[index+len(str(number_to_find)):]}")


fibonacci()
