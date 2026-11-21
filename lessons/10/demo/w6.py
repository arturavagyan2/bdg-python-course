# ## W6 · A lookup function can return a record
# Pass the records and search value into the function. Return the first match immediately; return None after the loop only when nothing matches. The caller uses is None to check for that missing result.
# 
# **Predict:** Why is return None after the loop?
# 
# **Try:** Try a missing name. is None checks for the special no-result value.
def find_room(rooms, target):
    for room in rooms:
        if room["name"] == target:
            return room
    return None

rooms = [{"name": "Studio", "seats": 8}]
room = find_room(rooms, "Studio")
if room is None:
    print("Not found")
else:
    print(room["seats"])
