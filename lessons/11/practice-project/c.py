# ## C · A wallet without hidden global changes · 14 min
# **Goal:** Replace shared state with an explicit input and returned balance.
# 
# Predict what the starter prints, then run it. Replace the global-based function with `spend(balance, amount)`. For a non-negative amount no larger than the balance, return the remaining balance. Otherwise return the original balance. Do not change a global variable or print inside.
# 
# Save the result of spending 12 from a wallet of 50. Test a separate wallet of 20 with a spend of 5. Save the returned value at the caller when you want a wallet to change.
# 
# **Check:** Results are 38 and 15. Spending 60 from 50 or spending -1 returns 50. Calls for the separate wallet must not affect the first wallet.
# 
# **Extra (optional):** Spend the exact remaining balance and check that the result is 0.

balance = 50

def spend(amount):
    global balance
    balance -= amount
    return balance

print(spend(12))
print(balance)
# Replace this version with the explicit-parameter function.
