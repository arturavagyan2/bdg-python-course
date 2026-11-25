# ## A · A delivery fee with useful defaults · 15 min
# **Goal:** Use positional, keyword and default arguments for one rule.
# 
# Write `delivery_fee(distance, rate=2, handling=1)`, returning distance × rate + handling. All supplied numbers are non-negative. Keep printing outside.
# 
# Call it three ways: distance 3 using defaults; distance 3 with handling 0 supplied by keyword; distance 3 with rate 4 and handling 2 supplied by keyword. Use a positional argument for the distance in the first two calls.
# 
# **Check:** Results are 7, 6 and 14. Explicit handling 0 stays zero. A call with every argument named may put the keyword arguments in a different order.
# 
# **Extra (optional):** Make an all-keyword call with handling first, then distance, then rate.

# Define delivery_fee and add the three calls.
