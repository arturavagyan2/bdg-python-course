# ## E · Contact book with record search · 30 min
# **Goal:** Use a list of dictionaries for a small menu with safe search and deletion.
# 
# Build a menu: 1 show all, 2 find by exact name, 3 delete by exact name, 0 exit.
# - Display every name and phone; for an empty book print "No contacts".
# - Find prints the matching phone or "Not found". Names in the supplied data are unique and matching is case-sensitive.
# - Delete removes just the matching record, or prints "Not found" without changing the list.
# - An unknown menu choice prints "Unknown choice" and asks again.
# Keep asking until 0. Phones stay text. Use fictional data only. Data resets when the program restarts. First get show/exit working, then find, then delete.
# 
# **Check:** Try show; find Lena; find Nora; delete Lena; find Lena again; delete Nora; show; 0. Only Bo/0202 should remain. Also delete both contacts and show the empty book. A missing name must never delete the last person.
# 
# **Extra (optional):** Show each contact with a display number starting at 1; keep name-based deletion unchanged.
contacts = [{"name": "Lena", "phone": "0101"},
            {"name": "Bo", "phone": "0202"}]
# Build your menu here. Do not define functions yet.
