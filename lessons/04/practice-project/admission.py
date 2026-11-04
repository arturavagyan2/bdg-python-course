# # E2 · Apply a fictional admission policy · 14 minutes
# 
# Build independently after W5. A fictional evening making session uses this exact safety policy. Read age as a nonnegative whole number and accompanying_adult as exact lowercase "yes" or "no". Assume valid entries.
# 
# - Under 12: print "Not admitted", even with an adult.
# - From 12 through 17 inclusive: print "Admit with adult" only if accompanying_adult is "yes"; otherwise print "Adult required".
# - Age 18 and above: print "Admit independently", regardless of the adult answer.
# 
# Choose the branch order and where an inner question is useful. Display exactly one admission decision and then "Decision recorded" outside the decision. Do not confuse a truthy "no" string with agreement. Plan the paths before writing code; do not copy the equipment-desk example without adapting the rule.
# 
# **Cases to predict/check:**11/yes→Not admitted;12/no→Adult required;12/yes→Admit with adult;17/yes→Admit with adult;18/no→Admit independently;19/yes→Admit independently. Include 18/yes too: two numerical ranges may be describable, but exactly one final decision should print.
# 
# **Optional extension:** show which shared yes/no test could be flattened using and without losing a needed explanation. Keep the four required decision messages intact.
