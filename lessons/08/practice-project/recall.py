# ## R · Keep an ordered queue · 8 min
# **Goal:** Retrieve the list operations needed for comparison with sets.
# 
# Predict the starter output before running it. Modify the code to serve the first person rather than the last. Print the served name and remaining queue.
# 
# **Check:** The original serves Nora. Your modified version serves Ali and leaves Lia then Nora.
# 
# **Extra (optional):** Predict what happens when the first two people have the same name. Keep both entries.

queue = ["Ali", "Lia", "Nora"]
served = queue.pop()
print(served)
print(queue)
