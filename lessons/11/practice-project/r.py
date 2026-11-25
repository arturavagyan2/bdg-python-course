# ## R · Return a value for a second caller · 8 min
# **Goal:** Recall parameters, returned results and separate display.
# 
# Repair `subtotal(price, quantity)` so it returns the multiplication instead of printing it. Save the cost of 3 items at price 4, then display that result and the result plus a single fee of 2. Call the same function with a different pair of arguments.
# 
# **Check:** The first two displayed numbers are 12 and 14. A call for price 5 and quantity 0 returns 0. The function itself prints nothing.
# 
# **Extra (optional):** Combine the results of two subtotal calls before printing.

def subtotal(price, quantity):
    print(price * quantity)

result = subtotal(4, 3)
print("Saved:", result)
