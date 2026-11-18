# ## W5 · enumerate adds a position
# enumerate gives a counter and the current item. By default the counter starts at zero and matches a list index. Starting at 1 is useful for display; that displayed number is then one more than the index.
# 
# **Predict:** What changes if the second argument is removed?
# 
# **Try:** Print the seat count beside each displayed booking number.
tickets = [{"name": "Mia", "seats": 2},
           {"name": "Noah", "seats": 1}]
for number, ticket in enumerate(tickets, 1):
    print(number, ticket["name"])
