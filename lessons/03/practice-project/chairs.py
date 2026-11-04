# A · Names and a stored total · 10 minutes
#
# Use assignment and reassignment deliberately. W1 has already explained names, =, multi-argument print and stored results.
#
# A room has ten ready chairs and three spare chairs. The starter calculates a total, then changes the ready count. Predict every output before running. Choose a clearer snake_case name for ready and rename its uses consistently. Change the ready count to fourteen, then add the recalculation needed so the final printed total describes the updated room. Keep the spare count unchanged.
#
# In your notes, explain why 2chairs and chairs ready are invalid names, and why Ready and ready are different. A name may be valid while still being less readable than snake_case.
#
# **Check after modification:** ready 14 and spare 3 must give final total 17. The starter's earlier stored total is a different point in the program; preserve it to explain what happened.
#
# **Optional extension:** change the spare count too, predict which stored values need recalculation and verify. Do not add input before W3.

ready = 10
spare_chairs = 3
chair_total = ready + spare_chairs
ready = 12
print("Ready now:", ready)
print("Stored total:", chair_total)
