import re

with open("../resources/day_06.txt") as f:
    lines = f.read().strip().split("\n")

time_values = re.findall(r'\d+', lines[0])
distance_values = re.findall(r'\d+', lines[1])

# Create tuples from the time and distance values
races = [(int(time), int(distance)) for time, distance in zip(time_values, distance_values)]

win_product = 1
for time, distance in races:
    win_count = 0
    for i in range(time):
        if ((time - i) * i) > distance:
            win_count += 1
    win_product *= win_count


# Part 1
print(win_product)

with open("../resources/day_06.txt") as f:
    lines = f.read().strip().split("\n")

time_values = re.findall(r'\d+', lines[0].replace(" ", ''))
distance_values = re.findall(r'\d+', lines[1].replace(" ", ''))

# Create tuples from the time and distance values
races = [(int(time), int(distance)) for time, distance in zip(time_values, distance_values)]

win_product = 1
for time, distance in races:
    win_count = 0
    for i in range(time):
        if ((time - i) * i) > distance:
            win_count += 1
    win_product *= win_count

# Part 2
print(win_product)
