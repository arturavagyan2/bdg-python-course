# E · Build a guessing game · 40 min
# Goal: Combine input, comparison, counting and loop termination.
# Choose a secret from 1 to 20 once. Keep asking for a whole-number guess. Print Higher if it is too low, Lower if it is too high. On a match, print Found in followed by the number of guesses, then stop. Count the winning guess too.
# Check with secret = 7 temporarily: guesses 3, 9, 7 → Higher, Lower, Found in 3. Restore random.randint before finishing.
# Extra: add quit using a text entry before int conversion.

import random
secret = random.randint(1, 20)
attempts = 0
# Ask, count, compare and stop.
