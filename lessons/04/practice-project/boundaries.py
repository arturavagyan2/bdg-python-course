# # C · Find a boundary and a shadowed rule · 10 minutes
# 
# Use W3 chains, branch priority and manual boundary checks. A fictional locker service assigns exactly one daily fee by nonnegative whole hours:0–2 hours inclusive cost 0;3–5 inclusive cost 2;6 or more cost 4. All fees are in credits. The starter runs but does not follow this policy.
# 
# Before editing, predict the fee at 6 and trace which condition wins. Repair the chain; keep exactly one fee. Use a useful order of thresholds rather than adding independent if statements. You may keep hours as an assigned number and change it between runs; no input is required here.
# 
# **Check below/at/above each transition:**1→0,2→0,3→2,4→2,5→2,6→4. Also check 0→0. Write expected and actual fee for each case. A successful run for 4 alone is not enough.
# 
# **Optional extension:** test 20 and explain which branch catches all larger valid counts.

hours = 6
if hours >= 3:
    print("Fee:", 2)
elif hours >= 6:
    print("Fee:", 4)
else:
    print("Fee:", 0)
