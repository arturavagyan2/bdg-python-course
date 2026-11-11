# X2: A tuple position cannot change
# This intentional error shows the meaning of immutable: Python refuses assignment to a tuple position. Read the TypeError. A tuple can still be replaced by assigning a new tuple to its variable.
# INTENTIONAL ERROR: TypeError
room = ("Room A", 12)
room[1] = 14
