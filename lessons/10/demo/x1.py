# ## X1 · A missing argument
# This example intentionally raises TypeError. A call must supply the required arguments. It is a call-time error rather than a syntax error. Default and keyword arguments come in lesson 11.
# 
# **Predict:** What required value is missing?
# 
# **Try:** Supply a unit price in a working copy.
def ticket_cost(count, unit_price):
    return count * unit_price

print(ticket_cost(3))
