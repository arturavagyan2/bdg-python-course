# ## E · Build a contact-book menu · 30 min
# **Goal:** Use unique names for safe lookup, update, delete and display.
# 
# Use fictional contacts only; nothing is saved to disk. Start with an empty dictionary mapping name to phone text. Menu: 1 add or update, 2 find, 3 delete, 4 show all pairs, 0 exit. A repeated name replaces its number. Missing find/delete prints Not found. Unknown choices print Unknown choice. Keep names exact; do not convert phone text to a number.
# 
# **Check:** Build add/show/exit first. Add Mira with 0101, update Mira to 0202, find Mira, show all, delete Mira, then find/delete her again. Only one Mira entry should exist; leading zero must remain; missing operations must not crash. Empty show prints No contacts.
# 
# **Extra (optional):** For show all, print names alphabetically using sorted(contacts), then look up each value. Keep update behavior unchanged.

contacts = {}
# Build add/show/exit first. Read phone numbers as text.
# Use membership before lookup or deletion.
