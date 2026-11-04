# R · Read a loop you already know · 8 min
# Goal: Trace existing for/if/break/continue code.
# Here for visits each character of the text in order. Predict the output without running. For the text abxc, skip b, stop at x, and print other letters. Then run and compare. Explain why c never prints.
# Change the text to bacx and predict again before running.
# Extra: what changes if the stop check is placed after print?

for letter in "abxc":
    if letter == "b":
        continue
    if letter == "x":
        break
    print(letter)
