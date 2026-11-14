# W5: Check a key before lookup or deletion
# Use membership before accessing a possibly missing key. This handles an expected missing entry without crashing. A fixed-key stock example differs from your contact-book task, which must read fresh names each turn.
stock = {"pens": 8, "pads": 3}
product = "glue"
if product in stock:
    print(stock[product])
else:
    print("No such product")
if "pads" in stock:
    del stock["pads"]
print(stock)
