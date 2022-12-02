import sys
from sortedcontainers import SortedList


def count_calories(input_file_name):
    with open(input_file_name, 'r') as f:
        lines = f.readlines()

    sorted_calories_list = SortedList()
    current_calories = 0
    for line in lines:
        if line != '\n':
            current_calories += int(line)
        else:
            sorted_calories_list.add(current_calories)
            current_calories = 0

    print('The sum of the 3 maximum calories is: %d' % (
                    sorted_calories_list[-1] + sorted_calories_list[-2] + sorted_calories_list[-3]))


if __name__ == '__main__':
    if len(sys.argv) > 1:
        file_name = sys.argv[1]
    else:
        file_name = "input.txt"
    count_calories(file_name)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
