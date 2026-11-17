robot = {
    "name": "Atlas",
    "model": "RX-7",
    "battery": 85,
    "speed": 6,
    "mode": "exploration"
}
print(f"The name is {robot["name"]} and the model is {robot["model"]}.\n")
robot["battery"] = 100
print(f"The battery is {robot["battery"]}.\n")
robot["color"] = "red"
print(f"The color is {robot["color"]}.\n")
robot.pop("mode")
print(f"There are {len(robot)} key-value pairs.\n")
for key, value in robot.items():
    print(f"Key: {key}, Value: {value}")