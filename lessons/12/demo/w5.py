from datetime import date, timedelta
import random

start = date(2026, 11, 28)
print(start + timedelta(days=7))
random.seed(7)
print(random.choice(["Mina", "Bo", "Nora"]))
