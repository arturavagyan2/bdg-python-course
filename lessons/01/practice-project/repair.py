# ## C · It crashes — and then it is still wrong · 12 minutes
#
# Learning objective: Repair a syntax error and separately check whether successful output contains the right information.
#
# Already taught: W3: read the final error message, match quotes/parentheses, save and rerun. # begins a comment for humans.
#
# The lost-property desk actually closes at 18:00. The starter has both a Python-writing mistake and an out-of-date closing time.
#
# 1. Run the starter as supplied. Record the final error type and the line Python points to. A traceback is diagnostic information, not your intended output.
# 2. Repair only the writing mistake first. Run again. Does the output now meet the desk’s request?
# 3. Update the closing time and run again. Record why a successful run alone was not enough.
# 4. Save a working copy. Deliberately remove one quotation mark, predict what will happen, and run once. Restore it and rerun successfully before finishing.
#
# Expected behavior: the final saved file runs without an error and clearly gives the correct desk and closing time. Your notes distinguish the punctuation repair from the information correction. Exact error wording may vary by Python version.
#
# Optional extension: Swap the two complete print lines. Predict and check the output order. Choose the order you find easier to read and explain why.

print("Lost-property desk")
print("Open until 17:00"
