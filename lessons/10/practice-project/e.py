# ## E · Refactor a working order checker · 30 min
# **Goal:** Give display, calculation and lookup separate reusable functions while preserving behavior.
# 
# Open the working program in the next code cell (also practice-project/refactor-start.py). Run it and try every menu choice before editing. Refactor means changing the organization while keeping the behavior.
# 
# Extract these functions above the menu:
# - show_order(order): print item/quantity lines, or "No items"; no meaningful return value.
# - order_total(order): return the sum of price * quantity; print nothing.
# - find_item(order, target): return the first matching record, or None; print nothing.
# 
# Replace the repeated menu code with calls. Keep input and menu decisions outside the functions. Pass order into each function. Use exact item names. Preserve choices 1 show, 2 total, 3 find, 0 exit and the missing/unknown messages. Do not change the data or add features until the behavior matches. You may use your own completed lesson-9 contact menu instead, with matching display/lookup functions and a separately named operation for deletion; agree its contracts with the instructor first.
# 
# **Check:** For the starter data: show displays soup 2 and bread 1; total is 8; find bread shows quantity 1 and price 2; find cake says Not found; an unknown choice says Unknown choice; 0 exits. The total function alone must return 8 without printing. Empty order: total 0, display No items, lookup None.
# 
# **Extra (optional):** Call order_total with a different one-item order to show that it uses its parameter rather than the original list.
# The working starter program is in the following cell.
# Edit that program in place; use this cell for quick function calls if useful.
