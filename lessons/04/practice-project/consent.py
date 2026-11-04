# # D · Repair consent and a blocking rule · 10 minutes
# 
# Debug W4 Boolean logic. A fictional reminder form accepts exact lowercase "yes" or "y" only when a do_not_contact flag is False. That flag blocks either accepted answer. Other words, including "no", are rejected. There are no case-normalization requirements yet.
# 
# Run the starter with its supplied values and explain why it accepts "no". Repair the expression so both comparisons are explicit and the blocking rule applies to both alternatives. Do not solve it by changing the test data or deleting the blocking requirement.
# 
# **Manual cases:**yes/False→"Reminder allowed"; y/False→allowed; no/False→"Reminder blocked"; yes/True→blocked; y/True→blocked. Write predictions first and record results. Explain what not changes and whether it modifies the flag itself.
# 
# **Optional extension:** compare your grouped condition with an ungrouped version on a blocked "yes". Explain the consequence before restoring the clear version.

answer = "no"
do_not_contact = False
if answer == "yes" or "y" and not do_not_contact:
    print("Reminder allowed")
else:
    print("Reminder blocked")
