# D · Ask until the reply is valid · 14 min
# Goal: Repeat input until a valid answer is entered.
# Keep asking for yes or no. Save either reply and end the loop. For anything else, print Please answer yes or no and ask again. Use .lower() so YES works too.
# Check: maybe, YES → one retry, then Saved: yes.
# Extra: let quit print Cancelled and stop without saving.

reply = input("Yes or no: ").lower()
# Add a loop and the reply checks.
