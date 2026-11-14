# W2: Compare two groups
# Union keeps everyone in either group; intersection keeps only people in both; difference keeps people in the first group who are absent from the second. Difference has a direction. These methods return new sets and leave the original groups alone.
morning = {"Ada", "Bo"}
evening = {"Bo", "Cy"}
print("Either:", sorted(morning.union(evening)))
print("Both:", sorted(morning.intersection(evening)))
print("Morning only:", sorted(morning.difference(evening)))
print("Evening only:", sorted(evening.difference(morning)))
