num = int(input("Enter a number with 5 digits:"))

ten_thousand = int(num / 10000)
thousand = int(num % 10000 / 1000)
hundreds = int(num % 1000 / 100)
dozens = int(num % 100 / 10)
units = int(num % 10)
sum_digits = ten_thousand + thousand + hundreds + dozens + units
print(f"You enter the number {num}")
print(f"The digits of the number are: {ten_thousand},{thousand},{hundreds},{dozens},{units}")
print(f"The sum of the digits is: {sum_digits}")


