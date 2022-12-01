with open("input.txt") as file:
    contents = file.readlines()

currentCalories = 0
maxCalories = [0, 0, 0]

for content in contents:
    if (content == "\n"):
        (maxCalories[0], temp) = (max(currentCalories,
                                      maxCalories[0]), min(currentCalories, maxCalories[0]))
        (maxCalories[1], temp) = (
            max(temp, maxCalories[1]), min(temp, maxCalories[1]))
        maxCalories[2] = max(temp, maxCalories[2])
        currentCalories = 0
    else:
        currentCalories += int(content)

print(maxCalories[0] + maxCalories[1] + maxCalories[2])
