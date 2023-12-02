import re


def main():
    file_path = '../resources/day_01.txt'
    # Part 1
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        print(f'Part 1 Answer: {sum_lines(file.read().splitlines())}')

    # Part 2
    with open(file_path, 'r', encoding='utf-8-sig') as file:
        print(f'Part 2 Answer: {sum_lines(replace(file.read()))}')


def sum_lines(lines) -> int:
    calibration_value = 0
    for line in lines:
        matches = re.findall(r'[0-9]', line)
        calibration_value += int(matches[0] + (matches[-1]))

    return calibration_value


def replace(data: str) -> list:
    return (
        data.replace("one", "one1one")
        .replace("two", "two2two")
        .replace("three", "three3three")
        .replace("four", "four4four")
        .replace("five", "five5five")
        .replace("six", "six6six")
        .replace("seven", "seven7seven")
        .replace("eight", "eight8eight")
        .replace("nine", "nine9nine")
    ).splitlines()


if __name__ == "__main__":
    main()
