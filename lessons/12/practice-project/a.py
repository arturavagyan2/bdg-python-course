# ## A · Compare separate and shared boxes · 15 min
# **Goal:** Use math.ceil for a useful rounding decision.
# 
# Import math and write `boxes_needed(item_count, capacity)`, returning enough boxes for all items. Count is a non-negative whole number and capacity is a positive whole number. Partly filled boxes still count.
# 
# For groups bringing 5 and 3 items, with capacity 4 per box, calculate boxes when each group packs separately and boxes when they share. Use your function in both calculations.
# 
# **Check:** Separate packing needs 3 boxes; shared packing needs 2. Zero items need 0 boxes; exact capacity needs 1. Explain why adding the two separately rounded results can differ from rounding the combined count.
# 
# **Extra (optional):** Test one item above a full box.

import math
# Define boxes_needed and compare the two packing plans.
