# E · Repair an average and update the facts · 8 minutes
#
# Apply W5. A student studies for 35 minutes in one session and 55 in another. The starter claims to calculate the mean session length. Predict it before running, then compare the result with a hand calculation. Add parentheses so the calculation answers the intended question.
#
# The student adds ten minutes to each session. Update both session values using +=, then recalculate the mean and print the new result. Explain why updating the two values alone does not change an earlier stored mean. Rewrite one += as an equivalent ordinary assignment in your notes.
#
# **Checks after repair:** original mean 45.0 minutes; after the two updates 55.0. Another starting case, 40 and 60, has mean 50.0 and updated mean 60.0. Use + and /, not a typed final answer.
#
# **Optional extension:** reverse the extra study time with -=, then recalculate. Explain why the stored mean needs another assignment.

first_minutes = 35
second_minutes = 55
mean_minutes = first_minutes + second_minutes / 2
print("Mean session:", mean_minutes)
