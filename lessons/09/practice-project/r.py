# ## R · Update a flat dictionary · 8 min
# **Goal:** Recall key lookup, updates and items before nesting them.
# 
# Predict the two printed lines. Then change the Studio extension to "108" and display every room and extension using items().
# 
# **Check:** Prediction: 101 and True. After your change, Studio has 108 and Kitchen still has 102. Keep extensions as text.
# 
# **Extra (optional):** Add a room, then delete it safely without changing the other entries.
extensions = {"Studio": "101", "Kitchen": "102"}
print(extensions["Studio"])
print("Kitchen" in extensions)
