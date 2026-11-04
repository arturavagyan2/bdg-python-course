# ## W4-G · Guided two-number calculator · 4 minutes inside W4
# After the label/row demonstration, build a small calculator with the instructor. The starter reads two numbers and displays their sum. Add clearly labelled difference (first minus second) and product results using the taught operators. Predict all three results before running. Then choose a different decimal pair and check by hand.
# 
# **Sample entries:** 6 and 2 → sum 8.0, difference 4.0, product 12.0. **Second check:** 4 and 1.5 → sum 5.5, difference 2.5, product 6.0. Labels may differ. Use the notebook area below or practice-project/calculator.py. No division, conditions or error handling is needed.
# 
# **Percentage check after the teacher's example:** A percentage means a number of hundredths. Work out 10% of 200 using the W4 pattern, then check your calculation in a new line. Do not type 20 as the answer. For an optional change, choose a new amount and percentage.

first_number = float(input("First number: "))
second_number = float(input("Second number: "))
print("Sum:", first_number + second_number)
