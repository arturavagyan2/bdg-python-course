total = 0
large_items = 0
for item in range(3):
    price = float(input("Price: "))
    total += price
    if price >= 10:
        large_items += 1
print("Total:", total)
print("Items at least 10:", large_items)
