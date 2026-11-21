# ## D · Find a price or report no result · 10 min
# **Goal:** Return a matched field from a record search and handle absence at the caller.
# 
# Write find_price(products, target). Return the matching product’s price, or None if it is absent. Names are unique and matching is exact. Print a found price using a call for "map". For "hat", check is None and print "Not found". Use a loop rather than a fixed list position.
# 
# **Check:** map returns 3, and hat produces Not found. Also test an empty list and a target in the second record; a first-record mismatch must not end the search.
# 
# **Extra (optional):** Add a product with price 0. Check that the caller treats 0 as a valid found price.
products = [{"name": "bag", "price": 8}, {"name": "map", "price": 3}]
# Define the function and add your calls.
