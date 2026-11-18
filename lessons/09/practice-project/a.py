# ## A · Find and change a nested value · 15 min
# **Goal:** Follow a list index and then a record key without replacing the surrounding data.
# 
# 1. In seats, mark the last seat in the first row as "reserved".
# 2. In bookings, change Lia’s seat count from 1 to 2.
# 3. Print the changed seat and Lia’s name/count. Leave all other data unchanged.
# 
# **Check:** seats[0] should end with reserved; its other two seats and the second row stay unchanged. Lia has 2 seats; Bo still has 3.
# 
# **Extra (optional):** Append a new booking record for Nora with 4 seats, then display every name and seat count.
seats = [["A1", "A2", "A3"], ["B1", "B2", "B3"]]
bookings = [{"name": "Bo", "seats": 3}, {"name": "Lia", "seats": 1}]
# Write your changes and output below.
