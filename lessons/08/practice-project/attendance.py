# ## A · Keep unique attendees · 15 min
# **Goal:** Remove duplicates and safely change a set.
# 
# Convert the supplied arrivals to a set. Add Sona twice, then remove Aram only if present. Print a sorted display, the unique count and whether Lilit is present.
# 
# **Check:** Final display has Lilit, Mari and Sona once each; count is 3; Lilit membership is True. Repeat the removal check to show it is safe.
# 
# **Extra (optional):** Try a new arrivals list containing only repeated copies of one name.

arrivals = ["Lilit", "Aram", "Lilit", "Mari", "Aram"]
# Make a set, update it and check membership.
