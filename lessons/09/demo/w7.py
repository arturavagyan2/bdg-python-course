# ## W7 · Build a new shape for a different question
# A list of records is useful for storing related fields. A list of names is useful for display. Build the names with a loop first, then compare the comprehension. Both create a new list; neither deletes records from stock.
# 
# **Predict:** Which part chooses the field, and which part filters the records?
# 
# **Try:** Change the zero to 2 and compare the two results.
stock = [{"item": "pens", "count": 4},
         {"item": "pads", "count": 0}]
available = []
for row in stock:
    if row["count"] > 0:
        available.append(row["item"])
print(available)
print([row["item"] for row in stock if row["count"] > 0])
