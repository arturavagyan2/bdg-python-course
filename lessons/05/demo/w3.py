while True:
    command = input("Command: ")
    if command == "wait":
        continue
    if command == "done":
        break
    print("Received:", command)
