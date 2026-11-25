# ## E · Build an event quote utility · 30 min
# **Goal:** Combine reusable functions with different argument patterns in one useful script.
# 
# Work in one file, `event_tools.py` (or the code cell). No imports are needed yet. Build these small functions:
# - `group_cost(people, price=4, booking_fee=0)`: return people × price + booking_fee.
# - `combine_costs(*costs)`: return the sum, or 0 with no costs.
# - `quote_record(event, **details)`: return `{"event": event, "details": details}`.
# - `apply_adjustment(total, operation)`: return the result of calling the supplied function with total.
# 
# Keep input and printing outside all four functions. Call them to quote 10 people at the default price, a room cost of 12 and snacks of 8. Apply a lambda that subtracts a discount of 5. Build a record for "Saturday club" containing `before_discount` and `final_total`, then print it.
# 
# **Check:** Before discount is 60 and final total is 55. A second quote must use its own arguments. `combine_costs()` returns 0; an empty set of record details stays an empty dictionary.
# 
# Work in steps: group cost and calls (7 min), combining costs (7), record and adjustment (10), independent checks (6). This file is a utility module you will learn to import in lesson 12.
# 
# **Extra (optional):** Build a second quote with 3 people at price 5, booking fee 2, room 4 and no discount.

# Write the four functions above the calling code.
# Then build and display the Saturday club quote.
