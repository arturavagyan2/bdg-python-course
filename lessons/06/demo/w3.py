found = False
for letter in "cat":
    if letter == "a":
        found = True
        print("Found a")
        break
if not found:
    print("No a")
