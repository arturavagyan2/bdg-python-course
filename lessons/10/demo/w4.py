# ## W4 · return ends the current call
# A return immediately sends a value back to the caller. A later line in the function does not run on that path. Every call can choose a different path from its argument.
# 
# **Predict:** Does age 11 reach the second return?
# 
# **Try:** Check age 13 and explain the boundary.
def entry_message(age):
    if age < 12:
        return "Come back later"
    return "Welcome"

print(entry_message(11))
print(entry_message(12))
