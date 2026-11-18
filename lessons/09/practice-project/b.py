# ## B · Repair the path and update two groups · 14 min
# **Goal:** Distinguish outer keys, inner keys and list values.
# 
# The first added line below puts a list at the wrong level. Remove that line. Add "Nora" to Friday’s members list. Increase Friday’s marker stock by 2. Print each day and its members, then Friday’s marker count. Keep Tuesday unchanged.
# 
# **Check:** Outer keys remain Friday and Tuesday only. Friday members: Ali then Nora; markers: 5. Tuesday members: Bo; markers: 1.
# 
# **Extra (optional):** Add "Lia" to Tuesday, then print the number of members per day.
club = {"Friday": {"members": ["Ali"], "stock": {"markers": 3}},
        "Tuesday": {"members": ["Bo"], "stock": {"markers": 1}}}
club["members"] = ["Nora"]  # This is the wrong level.
# Repair the update and display the required values.
