# E: Working order checker to refactor. Full instructions: e.py or practice.ipynb E.
order = [{"item": "soup", "price": 3, "quantity": 2},
         {"item": "bread", "price": 2, "quantity": 1}]
while True:
    choice = input("1 Show, 2 Total, 3 Find, 0 Exit: ")
    if choice == "0":
        break
    elif choice == "1":
        if not order:
            print("No items")
        for row in order:
            print(row["item"], row["quantity"])
    elif choice == "2":
        total = 0
        for row in order:
            total += row["price"] * row["quantity"]
        print(total)
    elif choice == "3":
        target = input("Exact item: ")
        found = None
        for row in order:
            if row["item"] == target:
                found = row
                break
        if found is None:
            print("Not found")
        else:
            print(found["quantity"], found["price"])
    else:
        print("Unknown choice")
