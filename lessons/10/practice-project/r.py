# ## R · Retrieve one nested field · 8 min
# **Goal:** Recall list-of-dictionary access before passing records to functions.
# 
# Predict the two printed values. Change the second record’s phone to "0303", then print the name and phone for every record. Explain what each bracket in contacts[1]["phone"] selects.
# 
# **Check:** Prediction: Ali then 0202. Only Ali’s phone changes; Nora’s remains 0101.
# 
# **Extra (optional):** Print the records with display numbers starting at 1.
contacts = [{"name": "Nora", "phone": "0101"}, {"name": "Ali", "phone": "0202"}]
print(contacts[1]["name"])
print(contacts[1]["phone"])
