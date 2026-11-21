# ## W7 · Each function has one job
# A function name should say what it does. Here one function calculates a total and another displays a result. Passing values explicitly makes each part easier to check with small examples. DRY means Don’t Repeat Yourself: keep a repeated rule in one place.
# 
# **Predict:** Which function could a different display reuse?
# 
# **Try:** Try an empty booking list. Do not add input prompts inside total_seats.
def total_seats(bookings):
    total = 0
    for booking in bookings:
        total += booking["seats"]
    return total

def show_total(total):
    print("Booked seats:", total)

bookings = [{"seats": 2}, {"seats": 3}]
show_total(total_seats(bookings))
