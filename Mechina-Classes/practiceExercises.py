# # Exercise 1:---Area and scope of rectangle---
# width = int(input("Enter width:"))
# length = int(input("Enter length:"))
# area = width * length
# scope = 2 * (width + length)
# print(f"The rectangle area is: {area}")
# print(f"The rectangle scope is: {scope}")
#
#
# # Exercise 2:---An employee salary per month---
# money_per_hour = int(input("Money per hour:"))
# hour_num = int(input("Hours of work this month:"))
# salary_per_month = money_per_hour * hour_num
# print(f"The employee get {money_per_hour} per hour, "
#       f"work {hour_num} hours, and all together gets {salary_per_month} per month.")
#
# # Exercise 3:---Kilometer to meter---
# kilometer = float(input("Enter Num of kilometers:"))
# meter = int(kilometer * 1000)
# print(f"The value of {kilometer} kilometers is {meter} meters.")
#
# # Exercise 4:---Get 2 numbers and switch the values---
# num1 = int(input("Enter first number:"))
# num2 = int(input("Enter second number:"))
# # Option 1: --With helping parameter--
# print(f"(With)Before: Num1- {num1}, Num2- {num2}")
# num3 = num1
# num1 = num2
# num2 = num3
# print(f"(With)After: Num1- {num1}, Num2- {num2}")
# # Option 2: --Without helping parameter--
# print(f"(Without)Before: Num1- {num1}, Num2- {num2}")
# num1 = num1 + num2
# num2 = num1 - num2
# num1 = num1 - num2
# print(f"(Without)After: Num1- {num1}, Num2- {num2}")

# # Exercise 5:---How much taxi we can fill with full sits?---
# taxis_num = int(input("Enter number of taxis:"))
# passengers = int(input("Enter number of passengers waiting:"))
# taxis_sits = taxis_num * 4
# passengers_per_taxi = 4
# if taxis_sits > passengers:
#     full_taxis_need = int(passengers / passengers_per_taxi)
#     passengers_in_station = int(passengers % passengers_per_taxi)
#     print(f"We can fill {full_taxis_need} taxis, but we stay in station {passengers_in_station} passengers.")
# elif taxis_sits < passengers:
#     extra_taxi_need = int(passengers / passengers_per_taxi) - taxis_num
#     passengers_in_station = int(passengers % passengers_per_taxi) + (extra_taxi_need * 4)
#     print(f"We can fill {taxis_num} taxis, but we stay in station {passengers_in_station} passengers.")


