robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}

while True:
    operation = input("\nWhat would you like to do?\n1. View all settings\n2. look up a setting\n3. Change a setting\n4. Add a setting\n5. Exit\n")
    if operation == "1":
        for key, value in robot.items():
            print(f"Key: {key}, Value: {value}")
    elif operation == "2":
        insert = input("What would you like to look up?\n")
        print(robot.get(insert, f"\n{insert} is not in the dictionary.\n"))
    elif operation == "3":
        insert = input("What key would you like to change?\n")
        if insert in robot.keys():
            insert_2 = input("What value would you like to change it to?\n")
            robot[insert] = insert_2
        else:
            print("That key does not exist.")
    elif operation == "4":
        insert = input("What key would you like to add?\n")
        insert_2 = input("What value would you like to add?\n")
        robot[insert] = insert_2
    elif operation == "5":
        break
    else:
        print("That operation does not exist. Please choose from '1, 2, 3, 4, 5'.")