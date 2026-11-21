# ## W3 · Printing does not return the printed number
# print displays something for a person. A function with no return value gives its caller None, meaning no result was supplied. That is why displaying a calculation is not enough when later code needs the number.
# 
# **Predict:** Does result contain 12?
# 
# **Try:** Trace which print runs inside the function and which runs in the caller.
def show_cost(count, price):
    print(count * price)

result = show_cost(3, 4)
print("Saved:", result)
