# ## C · Repair the extension directory · 14 min
# **Goal:** Use a key to replace a value and handle absence safely.
# 
# The starter adds an unwanted key instead of changing Reception. Repair it so Reception becomes "201". Add Studio with "205". Delete Archive only if it exists. Print the directory and check whether key "201" exists. Store extensions as text.
# 
# **Check:** Only Reception and Studio remain, with values "201" and "205". The key-membership check for "201" is False. Repeat the guarded Archive deletion safely.
# 
# **Extra (optional):** Check whether "201" appears among values using values() after W4 has been taught.

extensions = {"Reception": "200", "Archive": "209"}
extensions["201"] = "Reception"
# Fix the update. Add Studio and safely delete Archive.
