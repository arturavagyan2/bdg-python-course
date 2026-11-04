# # F · Compare rules with a language-model proposal · 10 minutes
# 
# Apply W6 to a different fictional shop inbox. Write a classifier with this priority: if the lowercased message contains "refund", print "Refund queue"; otherwise if it contains "delivery", print "Delivery queue"; otherwise print "Human review". Refund wins when both appear. Use a string, .lower(), membership and if/elif/else; no lists/loops/functions/API code.
# 
# Before running, write the rule label you expect for each fictional message:
# - M1: "Where is my delivery?"
# - M2: "Can you check my delivery or refund it?"
# - M3: "My parcel has not arrived."
# - M4: "I do not want a refund."
# 
# Run one message at a time by changing the starter's assigned text. Record actual label and the exact matching characters/first branch (or lack of a keyword). These are predictions for you to investigate; no expected rule outputs are supplied here.
# 
# **Then** open [ai-comparison.md](ai-comparison.md). Its responses are labelled synthetic proposals, not a live LLM run. For each message ask: does that proposal match the sender's words? Is intent clear? Where could the rule or proposal mislead? Keep original predictions, observations and explanations separate. You are checking meaning, not voting for one tool to always win.
# 
# **Optional extension:** change only the rule priority so delivery wins when both appear. Predict which of these cases could change; verify, then restore the original policy. No paid account or internet is required.

message = "Where is my delivery?"
# Normalize and write your priority chain below.
