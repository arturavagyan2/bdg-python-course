# ## D · Pass a pricing rule into a loop · 10 min
# **Goal:** Pass a function as a value and apply it to each item.
# 
# Write `transform_values(values, operation)`. Return a new list containing `operation(value)` for each input value, in order. Do not change the source list or print inside the function.
# 
# Use the supplied named function `add_fee` with prices `[2, 5, 0]`. Then use a lambda that doubles a value with the same list. Pass the function name, not the result of calling it.
# 
# **Check:** The two new lists are `[3, 6, 1]` and `[4, 10, 0]`. Empty input returns an empty list. The original list stays `[2, 5, 0]`.
# 
# **Extra (optional):** Use a lambda that turns each price into the Boolean result price > 3.

def add_fee(value):
    return value + 1

prices = [2, 5, 0]
# Define transform_values, then call it with add_fee and a lambda.
