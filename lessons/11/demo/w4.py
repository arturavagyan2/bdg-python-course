balance = 20

def spend(balance, amount):
    balance = balance - amount
    return balance

print(spend(balance, 3))
print(balance)
