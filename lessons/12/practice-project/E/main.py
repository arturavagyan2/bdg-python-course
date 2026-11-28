def line_cost(row):
    return row["price"] * row["quantity"]

def order_total(order):
    total = 0
    for row in order:
        total += line_cost(row)
    return total

def show_order(order):
    if not order:
        print("No items")
    for row in order:
        print(row["item"], row["quantity"], line_cost(row))

order = [{"item": "soup", "price": 3, "quantity": 2},
         {"item": "bread", "price": 2, "quantity": 1}]
while True:
    choice = input("1 Show, 2 Total, 0 Exit: ")
    if choice == "0":
        break
    elif choice == "1":
        show_order(order)
    elif choice == "2":
        print(order_total(order))
    else:
        print("Unknown choice")
