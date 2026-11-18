# ## C · Pair signup data without losing a person · 14 min
# **Goal:** Investigate zip stopping early, then transform matched values into numbered records.
# 
# 1. Predict which names the starter pairs, then run it.
# 2. Nora’s phone is "0033". Repair the missing source value.
# 3. If the list lengths match, use zip and a loop to build records with name and phone keys. Otherwise print "Check the source lists" and build no records.
# 4. Use enumerate starting at 1 to display each record’s number, name and phone.
# 
# **Check:** The starter pairs Ali/0011 and Bo/0022 only. The repaired record list has all three people, numbered 1–3. A mismatch must produce a warning, not a silently incomplete record list.
# 
# **Extra (optional):** Change the display counter to start at 0. Explain why this does not change the records.
names = ["Ali", "Bo", "Nora"]
phones = ["0011", "0022"]
for name, phone in zip(names, phones):
    print(name, phone)
# Repair the source data, then build and display the records.
