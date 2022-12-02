import sys


def count_calories(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = f.readlines()

    current_max = 0
    current_calories = 0
    for line in lines:
        if line != '\n':
            current_calories += int(line)
        else:
            current_max = max(current_max, current_calories)
            current_calories = 0

    print('The maximum are %d calories' % current_max)


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = 'input.txt'
    count_calories(file_name)
