# ## B · A receipt with flexible prices and details · 14 min
# **Goal:** Use *args for prices and **kwargs for named receipt details.
# 
# Write `make_receipt(customer, *prices, **details)`. Return a dictionary with keys `customer`, `total` and `details`. Total is the sum of every supplied price; details is the collected keyword dictionary. Do not ask for input or print inside the function.
# 
# Call it for Lia with prices 3 and 4, paid=True and method="cash". Also call it for Bo with no prices or details. Prices are non-negative numbers.
# 
# **Check:** Lia’s total is 7 and both named details are kept. Bo’s total is 0 and details is an empty dictionary. Repeated equal prices still count separately.
# 
# **Extra (optional):** Add a third price and a new currency detail without changing the definition.

# Define make_receipt(customer, *prices, **details), then make two calls.
