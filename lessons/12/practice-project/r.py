# ## R · Use a named argument and a default · 8 min
# **Goal:** Retrieve lesson 11 argument patterns before moving code into files.
# 
# Complete `line_cost(price, quantity=1)` so it returns price × quantity. Print a call for price 4 using the default quantity, then a call with quantity 3 and price 4 named in that order. Keep printing outside.
# 
# **Check:** Results are 4 and 12. A named quantity of 0 must return 0. Explain which names are parameters and which values are arguments.
# 
# **Extra (optional):** Call the function with a decimal price.

def line_cost(price, quantity=1):
    return price  # Quantity is still ignored.

# Add and test your calls.
