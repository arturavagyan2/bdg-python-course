# # R · Retrieve a numeric script · 8 minutes
# 
# Recall lesson 3 before learning new syntax. Predict the result when 3 people each need 2.5 metres of ribbon, then run the starter. Change only the number of people to 4 and rerun. Explain why the old total does not update until its calculation runs again.
# 
# **Expected behavior:** original total 7.5 metres; changed total 10.0. Explain why float is suitable for a fractional measurement and input still needs conversion. Use this script/notebook, not your HW1 files. No new homework change is required.
# 
# **Optional extension:** replace the price/length with another decimal measurement and hand-check one run.

people = 3
metres_per_person = 2.5
total_metres = people * metres_per_person
print("Total metres:", total_metres)
