# Exercise 1: ---Shopping exercise---
prices = {
    'bananas': 10,
    'apples': 8,
    'bread': 7,
    'cheese': 20,
    'juice': 15
}
shopping_cart = {
    'bananas': 2,
    'bread': 1,
    'cheese': 3,
    'cheese234': 324
}
print(shopping_cart.values())
print(prices.values())

total = 0
for s in shopping_cart.keys():
    for p in prices.keys():
        if s == p:
            total += shopping_cart[s] * prices[p]
    if s not in prices.keys():
        print(f"The item '{s}' is not exist, sorry.")
print(f"The total of your shopping is: {total}")
