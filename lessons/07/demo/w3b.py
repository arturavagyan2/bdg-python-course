# W3b: A short list comprehension
# A comprehension builds a new list from a loop and an expression. Read [price - 1 for price in prices] as: for each price, keep price - 1. A final if keeps only matching items. Use a regular loop when several actions or input make the code easier to follow.
prices = [3, 6, 9]
reduced = [price - 1 for price in prices]
small = [price for price in prices if price <= 6]
print(reduced)
print(small)
print(prices)
