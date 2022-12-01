with open("input.txt") as file:
    contents = file.readlines()

currentCalories = 0
maxCalories = 0

for content in contents:
    if (content == "\n"):
        maxCalories = max(currentCalories, maxCalories)
        currentCalories = 0
    else:
        currentCalories += int(content)

print(maxCalories)
