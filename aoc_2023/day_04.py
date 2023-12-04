import re

with open("../resources/day_04.txt") as f:
    lines = f.read().strip().split("\n")

score = 0
for line in lines:
    line = line[line.index(':') + 1:].strip()
    parts = line.split('|')

    winning_numbers = set(map(int, re.findall(r'\d+', parts[0])))
    draw_numbers = set(map(int, re.findall(r'\d+', parts[1])))

    card_score = 0
    for number in draw_numbers:
        if number in winning_numbers:
            if card_score == 0:
                card_score += 1
            else:
                card_score = card_score * 2

    score += card_score

# Part 1
print(score)

# Part 2
# print()
