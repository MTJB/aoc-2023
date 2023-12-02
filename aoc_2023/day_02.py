import re
from functools import reduce


def main():
    file_path = '../resources/day_02.txt'
    print(f'Part 1 Answer: {sum_valid_games(file_path)}')
    print(f'Part 2 Answer: {sum_powers(file_path)}')


def sum_valid_games(file_path) -> int:
    limits = {"red": 12, "green": 13, "blue": 14}
    valid_game_ids = 0

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            valid_game_ids += get_valid_game_id(line, limits)

    return valid_game_ids


def get_valid_game_id(game_string, limits):
    game_id_match = re.search(r'Game (\d+):', game_string)
    if not game_id_match:
        return 0

    game_id = int(game_id_match.group(1))
    game_data = game_string.replace(game_id_match.group(0), '')

    for game_set in game_data.split(';'):
        for number, color in re.findall(r'(\d+) (\w+)', game_set):
            if int(number) > limits.get(color, float('inf')):
                return 0

    return game_id


def sum_powers(file_path) -> int:
    sum_of_powers = 0

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            sum_of_powers += find_power(line)

    return sum_of_powers


def find_power(game_string):
    game_id_match = re.search(r'Game (\d+):', game_string)
    if not game_id_match:
        return 0

    game_data = game_string.replace(game_id_match.group(0), '')

    max_values = {"red": 0, "green": 0, "blue": 0}
    for game_set in game_data.split(';'):
        for number, color in re.findall(r'(\d+) (\w+)', game_set):
            if int(number) > max_values.get(color, float('inf')):
                max_values[color] = int(number)

    return reduce(lambda x, y: x * y, max_values.values())


if __name__ == "__main__":
    main()
