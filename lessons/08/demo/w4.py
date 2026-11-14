# W4: Loop over dictionary entries
# keys() provides keys, values() provides values and items() provides pairs. Unpack each pair into two names, as with a tuple. A normal for loop over a dictionary visits its keys. Dictionaries preserve insertion order, but lookup uses a key rather than its position.
prices = {"tea": 2, "cake": 4}
print(list(prices.keys()))
print(list(prices.values()))
for product, price in prices.items():
    print(product, price)
