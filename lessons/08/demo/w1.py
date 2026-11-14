# W1: Keep each name once
# A set keeps unique values. It is useful for attendance or tags when duplicates are unwanted. Sets have no defined display order or numeric indexes. sorted makes a separate list for predictable display; it does not change the set. Use set() for an empty set; {} is an empty dictionary.
arrivals = ["Mia", "Noah", "Mia"]
present = set(arrivals)
print(sorted(present))
print(len(present))
print("Mia" in present)
present.add("Lena")
present.remove("Noah")
print(sorted(present))
