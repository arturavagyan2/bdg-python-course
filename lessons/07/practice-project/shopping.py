# ## E · Build a shopping-list menu · 30 min
# **Goal:** Keep and safely change one list across repeated choices.
# 
# Start with an empty list. Menu: 1 add an item, 2 remove an item by name, 3 search by name, 4 sort, 5 show, 0 exit. Missing removal/search prints Not on list. Sorting uses alphabetical order; showing prints the list (including [] when empty). Unknown choices print Unknown choice. Match names exactly; duplicates are allowed.
# 
# **Check:** Build add/show/exit first. Then test adding rice and apples, showing, searching rice, sorting, removing rice, showing again, removing rice again, and exiting. The final list contains only apples; missing removal must not crash.
# 
# **Extra (optional):** For add, reject a name already present. Keep this optional and explain the changed duplicate rule.

items = []
# Add/show/exit first. Keep items outside the loop.
# For removal, check membership before remove.
