from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def get_letter_value(letter: chr):
    return ord(letter) - ord('A') + 27 if letter.isupper() else ord(letter) - ord('a') + 1


class Task03(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of priorities of the items that appear in both compartments is: %d'
        self.bonus_answer_text = 'The sum of all badges is: %d'
        self.task_number = 3

    def solve_task(self, input_file_content: List[str]):
        current_sum = 0
        for line in input_file_content:
            line = line.replace('\n', '')
            first_compartment = sorted(line[0:len(line) // 2])
            second_compartment = sorted(line[len(line) // 2:])
            current_sum += sum(set([get_letter_value(x) for x in first_compartment if x in second_compartment]))
        return current_sum

    def solve_bonus_task(self, input_file_content: List[str]):
        current_sum = 0
        for i in range(0, len(input_file_content), 3):
            backpacks = [set(x.replace('\n', '')) for x in input_file_content[i: i + 3]]
            letters_in_all_lists = backpacks[0].intersection(backpacks[1]).intersection(backpacks[2])
            current_sum += sum([get_letter_value(x) for x in letters_in_all_lists])
        return current_sum

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            [line.replace('\n', '').isalpha() and len(line.replace('\n', '')) % 2 == 0 for line in input_file_content])
