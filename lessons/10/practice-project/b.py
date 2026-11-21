# ## B · Repair a result that disappears · 14 min
# **Goal:** Debug print-versus-return and leave display decisions to the caller.
# 
# Predict what the starter prints. Repair rectangle_area so it returns the area without printing inside the function. Save the area for a 4 by 3 room, then print it and the area plus a spare allowance of 2. Add a second call for a 2 by 5 room.
# 
# **Check:** The starter prints 12 and Saved: None. After repair, the three requested numerical results are 12, 14 and 10. Calling the function alone in a script should display nothing.
# 
# **Extra (optional):** Return the result of the expression rectangle_area(2, 3) + rectangle_area(1, 4) to a variable and print it.
def rectangle_area(length, width):
    print(length * width)

area = rectangle_area(4, 3)
print("Saved:", area)
# Repair the function, then use its returned value.
