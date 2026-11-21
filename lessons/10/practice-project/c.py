# ## C · Count available products · 14 min
# **Goal:** Put a loop inside a function and return only after examining all values.
# 
# Write count_available(stock). stock is a dictionary mapping item names to quantities. Return the number of products with quantity greater than zero, not the total units. Print calls for the supplied dictionary, an empty dictionary, and a dictionary containing only zero quantities. Keep the print calls outside the function.
# 
# **Check:** The results are 2, 0 and 0. If the first product has zero stock but the second is available, the result must still count the second.
# 
# **Extra (optional):** Write count_low(stock, limit), returning how many products have quantity below the supplied limit. Zero counts as low when limit is positive.
stock = {"pens": 3, "pads": 0, "clips": 2}
# Define count_available(stock), then call it with the three cases.
