# ## X1 · A key at the wrong level
# This example intentionally raises KeyError. A nested key is only available inside its containing dictionary. Read the traceback and identify the level where the lookup fails.
# 
# **Predict:** Where does the pens key actually live?
# 
# **Try:** Use the full path in a working copy.
rooms = {"Studio": {"supplies": {"pens": 4}}}
print(rooms["pens"])
