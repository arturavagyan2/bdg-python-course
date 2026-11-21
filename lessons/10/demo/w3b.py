# ## W3b · Return lets the caller choose what to do
# return supplies a value without displaying it. The caller can print that value, add a fee, or compare it. Keep the calculation in one place so one change fixes every call.
# 
# **Predict:** Would a call on its own print anything in a script?
# 
# **Try:** Use the returned result in a comparison with 10.
def calculate_cost(count, price):
    return count * price

result = calculate_cost(3, 4)
print("Saved:", result)
print("With fee:", result + 2)
