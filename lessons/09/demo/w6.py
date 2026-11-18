# ## W6 · zip pairs matching positions
# zip takes one item from each list per turn. It pairs positions, not matching names. It stops when the shorter list ends, so check lengths when every input must become a record. This lesson uses a length check, without exceptions.
# 
# **Predict:** Will Bo appear? Why?
# 
# **Try:** Add a seat count for Bo and run again.
names = ["Mia", "Noah", "Bo"]
seats = [2, 1]
for name, count in zip(names, seats):
    print(name, count)
print("Lengths:", len(names), len(seats))
