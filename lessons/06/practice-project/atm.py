# E · Build a small ATM menu · 23 min
# Goal: Preserve state while handling menu choices.
# Start with 50 credits. Repeat a menu: 1 shows balance; 2 reads a deposit and adds it; 3 reads a withdrawal and subtracts it only when it does not exceed the balance; 0 exits. Print Not enough credits when a withdrawal is too large. Unknown choices print Choose 0, 1, 2 or 3. Assume positive numeric amounts.
# Check: deposit 20, withdraw 15, show balance → Balance: 55.0. Then try withdrawing 60: the balance must stay 55.0. This is a simulation, not a real banking system.
# Extra: reject zero and negative amounts without changing the balance.

balance = 50.0
# Keep balance outside the menu loop.
