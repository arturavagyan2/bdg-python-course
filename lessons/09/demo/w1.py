# ## W1 · A list can hold rows
# Each outer-list item is another list. Read one bracket at a time: seats[1] selects a row, then [0] selects a seat. Changing that seat keeps the other seats in place.
# 
# **Predict:** Which bracket chooses the row?
# 
# **Try:** Change the last seat in the first row. Predict which values remain unchanged.
seats = [["A1", "A2"], ["B1", "B2"]]
print(seats[1])
print(seats[1][0])
seats[1][0] = "reserved"
print(seats)
