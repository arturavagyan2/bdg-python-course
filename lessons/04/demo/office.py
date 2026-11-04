message = input("Office message: ")
normalized = message.lower()
if "urgent" in normalized:
    print("Urgent review")
elif "invoice" in normalized:
    print("Accounts")
else:
    print("Human review")
