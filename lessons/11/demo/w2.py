def total_duration(*durations):
    total = 0
    for minutes in durations:
        total += minutes
    return total

print(total_duration(10, 5, 15))
print(total_duration())
