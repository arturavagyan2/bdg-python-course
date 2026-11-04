# C · Repair a numeric input · 12 minutes
#
# Debug after W3, using only taught conversion and addition. The ribbon desk needs a requested length plus 0.5 metres of spare ribbon. Run the supplied starter with 5 first. Record the error type and explain what types reached +. Repair the code so decimal lengths also work; do not change the required spare amount or convert a numeric result into text to hide the problem.
#
# **Sample entries and checks after repair:** 5 must produce 5.5 metres; 2.25 must produce 2.75 metres. Use type() temporarily if it helps you investigate, then leave clear reader output.
#
# Try the word five once after saving a working version. Record the conversion error, restore valid inputs and finish with a successful run. We observe invalid input; do not add try/except, loops or conditions. Required behavior assumes valid positive numeric entries.
#
# **Optional extension:** compare int("2.25") with float("2.25") in a separate scratch cell and explain why the first conversion fails.

requested_metres = input("Ribbon metres: ")
spare_metres = 0.5
total_metres = requested_metres + spare_metres
print("Ribbon including spare:", total_metres)
