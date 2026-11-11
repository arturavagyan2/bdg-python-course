# W2: Change a list
# append adds at the end; insert chooses a position. remove deletes the first matching value; pop removes and returns an item (the last by default). sort changes the same list into ascending order. These methods change the list; append and sort return None, meaning no result value.
queue = ["Ben", "Dina"]
queue.append("Eli")
queue.insert(1, "Cara")
queue.remove("Dina")
served = queue.pop(0)
queue.sort()
print("Served:", served)
print("Waiting:", queue)
