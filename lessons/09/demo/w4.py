# ## W4 · Keys can lead through several levels
# A value can itself be a dictionary. Follow the path from room to supplies to item. Each bracket works on the value produced by the previous bracket. Write a path on paper before editing a deep value.
# 
# **Predict:** Which keys exist directly inside rooms?
# 
# **Try:** Change open to False without replacing the whole Studio dictionary.
rooms = {"Studio": {"supplies": {"pens": 4}, "open": True}}
print(rooms["Studio"]["supplies"]["pens"])
rooms["Studio"]["supplies"]["pens"] += 2
print(rooms["Studio"]["supplies"]["pens"])
