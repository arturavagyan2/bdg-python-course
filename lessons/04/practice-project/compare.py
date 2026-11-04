# # A · Predict a comparison, then choose a type · 8 minutes
# 
# Use W1 comparisons to investigate a fictional stock check. Before running, predict both starter outputs. Then add a meaningful name for the numeric comparison result and print it.
# 
# A cupboard has 8 notebooks and 8 bookings. Add comparisons for equality, difference, strictly more, strictly fewer, enough (>=) and at most (<=). Write predictions first, check all six, then change bookings to 9. Do not convert a real shelf label merely because it contains digits.
# 
# **Expected behavior:** with equal counts, equality and both inclusive comparisons are True; strict inequalities and difference are False. With 9 bookings, explain each changed result. The text comparison must be explained from its characters, not from numeric size. Do not write branches yet.
# 
# **Optional extension:** compare "cat" and "catalog" and explain the prefix rule.

shelf_text = "12"
print("Text comparison:", shelf_text < "3")
print("Numeric comparison:", int(shelf_text) < 3)
