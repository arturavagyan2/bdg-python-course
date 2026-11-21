# ## W2 · Parameters receive values from a call
# A parameter is a name in the definition. An argument is a value supplied by a call. Each call runs the same calculation with its own values. return sends the result back so the caller can save or combine it.
# 
# **Predict:** Which names are parameters? Which values are arguments?
# 
# **Try:** Change the second call to 5 tickets at a price of 2.
def ticket_cost(count, unit_price):
    return count * unit_price

cost = ticket_cost(3, 4)
print(cost)
print(ticket_cost(2, 4) + 1)
