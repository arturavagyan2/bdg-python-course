# W1: Read part of a list
# A list keeps several values in order. Index 0 is the first item; -1 is the last. A slice stops before its end index, so [1:3] selects indexes 1 and 2.
items = ["tea", "rice", "soap", "apples"]
print(items[0], items[-1])
print(items[1:3])
print(items[:2])
print(items[2:])
items[1] = "pasta"
print(items)
print(len(items))
