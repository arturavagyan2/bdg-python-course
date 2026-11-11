# W4: Unpack a fixed pair
# A tuple keeps ordered values whose positions cannot be reassigned. Use it for a fixed pair such as a room and its capacity; use a list for a changing queue. Unpacking puts each value into a separate name. The number of names must match the number of values. A one-item tuple needs a comma: ("Room A",).
room = ("Room A", 12)
name, seats = room
print(name)
print("Seats:", seats)
print(room[0])
print(("Room B",))
