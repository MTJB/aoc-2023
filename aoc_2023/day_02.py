import re


def main():
    file_path = '../resources/day_02.txt'
    # Part 1
    print(f'Part 1 Answer: {sum_valid_games(file_path)}')


def sum_valid_games(file_path) -> int:
    limits = {"red": 12, "green": 13, "blue": 14}
    valid_game_ids = 0

    with open(file_path, 'r', encoding='utf-8-sig') as file:
        for line in file:
            valid_game_ids += process_game_line(line, limits)

    return valid_game_ids


def process_game_line(game_string, limits):
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


if __name__ == "__main__":
    main()
