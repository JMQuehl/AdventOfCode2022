from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def get_letter_value(letter: chr):
    return ord(letter) - ord('A') + 27 if letter.isupper() else ord(letter) - ord('a') + 1


class Task03(AdventOfCodeProblem):
    def __init__(self):
        super().__init__()
        self.answer_text = 'The sum of priorities of the items that appear in both compartments is: %d'
        self.bonus_answer_text = 'The second part of the question is not yet known: %d'
        self.task_number = 3

    def solve_task(self, input_file_content: List[str]):
        current_sum = 0
        for line in input_file_content:
            line = line.replace('\n', '')
            first_compartment = sorted(line[0:len(line) // 2])
            second_compartment = sorted(line[len(line) // 2:])
            letters_in_both = [x for x in first_compartment if x in second_compartment]
            current_sum += sum(set([get_letter_value(x) for x in first_compartment if x in second_compartment]))
        return current_sum

    def solve_bonus_task(self, input_file_content: List[str]):
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        for line in input_file_content:
            pure_line = line.replace('\n', '')
            if not pure_line.isalpha() or not len(line) % 2 != 0:
                return False
        return True
