# # Exercise 1: ---Shopping exercise---
# prices = {
#     'bananas': 10,
#     'apples': 8,
#     'bread': 7,
#     'cheese': 20,
#     'juice': 15
# }
# shopping_cart = {
#     'bananas': 2,
#     'bread': 1,
#     'cheese': 3,
#     'cheese234': 324
# }
# print(shopping_cart.values())
# print(prices.values())
#
# total = 0
# for s in shopping_cart.keys():
#     for p in prices.keys():
#         if s == p:
#             total += shopping_cart[s] * prices[p]
#     if s not in prices.keys():
#         print(f"The item '{s}' is not exist, sorry.")
# print(f"The total of your shopping is: {total}")


# My own exercise: ---Real customer enter data---
# first: print to him the shopping menu
prices = {
    'bananas': 10,
    'apples': 8,
    'bread': 7,
    'cheese': 20,
    'juice': 15
}
print("Hello customer, here is example of how to shop here: \n"
      "Enter your shopping: bananas 3 bread 1 cheese 2 \n Hope you will enjoy, have fun :) \n"
      f"Here is your options and their cost: {prices} \n")
shopping_s = input("Enter your shopping:")
shopping_l = shopping_s.split(" ")
shopping_cart = {}
for i in range(len(shopping_l)):
    try:
        if not shopping_l[i].isdigit():
            shopping_cart[shopping_l[i]] = int(shopping_l[i + 1])
    except:
        pass
print(shopping_cart)
total = 0
for s in shopping_cart.keys():
    for p in prices.keys():
        if s == p:
            total += shopping_cart[s] * prices[p]
    if s not in prices.keys():
        print(f"The item '{s}' is not exist, sorry.")
print(f"The total of your shopping is: {total}")
