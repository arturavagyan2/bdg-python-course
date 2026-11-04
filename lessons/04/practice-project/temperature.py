# # B · Modify a two-path temperature notice · 10 minutes
# 
# Apply W2 if/else and indentation. A fictional cold-storage check accepts a temperature of 8°C or lower; anything above 8 needs cooling. Inputs are valid numeric temperatures and may be negative.
# 
# Predict the starter with 8 before running. Modify its condition to match the rule, then read a temperature with input and float instead of fixing it in the source. Keep the final “Reading recorded” message outside the decision so it appears for every valid entry.
# 
# **Manual checks:** 7.5→"Storage accepted",8→"Storage accepted",8.5→"Cooling needed"; every run ends with "Reading recorded". Write expected results before each run. Use only the two taught paths.
# 
# **Optional extension:** temporarily indent the final message into one branch. Predict which case loses that line, observe, then restore the required behavior.

temperature_c = 8
if temperature_c < 8:
    print("Storage accepted")
else:
    print("Cooling needed")
print("Reading recorded")
