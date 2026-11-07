while True:
    choice = input("1: km to metres, 0: exit: ")
    if choice == "0":
        break
    elif choice == "1":
        km = float(input("Kilometres: "))
        print("Metres:", km * 1000)
    else:
        print("Choose 0 or 1")
