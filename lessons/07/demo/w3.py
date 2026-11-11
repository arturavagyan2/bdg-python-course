# W3: Build a new list with a loop
# Start with an empty result. Visit each price, calculate a new value and append it. The original prices stay unchanged.
prices = [3, 6, 9]
reduced = []
for price in prices:
    reduced.append(price - 1)
print(reduced)
print(prices)
