# ## C · Choose sessions that fit · 14 min
# **Goal:** Transfer a loop into a filter and a calculation.
# 
# Using the supplied durations, first build a list containing sessions of at most 20 minutes using a regular loop. Then write the same filter as a comprehension. Separately create a new list adding 5 minutes to every original session. Print all results and the original list.
# 
# **Check:** Both filters keep 10 and 20. The adjusted list has one value per original session. The original list stays unchanged.
# 
# **Extra (optional):** Change the limit to 5 and explain the empty result.

durations = [10, 25, 20, 35]
# First a loop, then a comprehension. Keep the original list.
