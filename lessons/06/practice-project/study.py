# B · Add study time · 15 min
# Goal: Transfer total and count patterns to entered data.
# Read minutes studied on three days. Print total minutes and how many days reached at least 20 minutes. Assume nonnegative whole numbers.
# Check 10, 20, 35 → Total: 65 and Target days: 2. Check 0, 0, 0 too.
# Extra: let the user choose how many days to enter.

total = 0
target_days = 0
for day in range(3):
    minutes = int(input("Minutes: "))
    # Update total and count target days.
print("Total:", total)
print("Target days:", target_days)
