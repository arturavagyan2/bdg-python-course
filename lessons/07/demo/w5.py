# W5: Keep a list between menu turns
# This small playlist adds a title, displays the list or exits. The list is created before the loop, so earlier titles survive the next turn. Read the choice inside the loop. Your shopping manager will need more choices and a guarded removal. item in items checks whether a value is present in a list; check before remove so a missing value does not cause ValueError.
titles = []
while True:
    choice = input("1 add, 2 show, 0 exit: ")
    if choice == "0":
        break
    elif choice == "1":
        title = input("Title: ")
        titles.append(title)
    elif choice == "2":
        print(titles)
    else:
        print("Unknown choice")
