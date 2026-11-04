# B · Repair a countdown · 16 min
# Goal: Repair a while condition and make the start configurable.
# The starter should print 4, 3, 2, 1, then Lift off. It currently prints nothing but Lift off. Fix the condition. Keep the counter change inside the loop.
# Then ask the user for the starting number. Check starts 1 and 5. Assume a positive whole number.
# Extra: make a for version with a negative range step.

seconds = 4
while seconds < 0:
    print(seconds)
    seconds -= 1
print("Lift off")
