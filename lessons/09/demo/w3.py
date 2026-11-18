# ## W3 · A dictionary can group lists
# A dictionary value can be a list. A key selects a group and append changes that group’s list. A loop over items() gives the group name and its list, rather than one member at a time.
# 
# **Predict:** Does append add a new team key?
# 
# **Try:** Make the evening group empty and check the count.
teams = {"morning": ["Mia"], "evening": ["Noah", "Bo"]}
teams["morning"].append("Lia")
for team, names in teams.items():
    print(team, len(names))
print(teams["morning"][1])
