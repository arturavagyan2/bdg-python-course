visits = 0

def record_visit():
    global visits
    visits += 1
    return visits

print(record_visit())
print(record_visit())
