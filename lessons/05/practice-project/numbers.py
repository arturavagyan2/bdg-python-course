# C · Skip an entry or stop asking · 17 min
# Goal: Apply skip and stop to repeated input.
# Keep asking for a whole number. Zero ends the program. A negative number is skipped with continue. For a positive number, print Double: followed by twice that number. Read a new number on every turn.
# Check: -2, 4, 0 gives only Double: 8, then stops. Try 0 first and then try two negative entries before 3 and 0.
# Extra: print Skipped for a negative number, but keep asking.

# Incomplete: add the stop check before running. Ctrl+C stops a stuck run.
while True:
    number = int(input("Number (0 to stop): "))
    # Stop, skip, or print the double.
