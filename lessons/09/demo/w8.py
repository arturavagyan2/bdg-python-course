# ## W8 · Find a position before removing a record
# A list has positions rather than name keys. Search the records and remember the matching index. After the search, remove that position only when a match exists. An index of -1 means not found in this program, so it must be checked before pop.
# 
# **Predict:** Why would pop(-1) be dangerous when a tag is missing?
# 
# **Try:** Search for an absent tag. The list must stay unchanged.
items = [{"tag": "K1", "item": "keys"},
         {"tag": "B2", "item": "bag"}]
found_index = -1
for index, item in enumerate(items):
    if item["tag"] == "K1":
        found_index = index
        break
if found_index != -1:
    items.pop(found_index)
print(items)
