# W3: Look up a value by its key
# A dictionary connects each unique key with a value. Here a product name is the key and its stock count is the value. Square brackets use the key, not a numeric position. Assignment adds a missing key or replaces its old value. del deletes one entry.
stock = {"pens": 8, "pads": 3}
print(stock["pens"])
stock["pens"] = 6
stock["clips"] = 10
del stock["pads"]
print(stock)
print("pens" in stock)
print(6 in stock)
