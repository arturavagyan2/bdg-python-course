def booking_cost(people, price=3, fee=1):
    return people * price + fee

print(booking_cost(2))
print(booking_cost(2, fee=0))
print(booking_cost(price=4, people=2, fee=1))
