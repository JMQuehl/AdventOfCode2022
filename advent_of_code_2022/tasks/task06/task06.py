from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


def find_first_occurrence_of_distinct_letters(input_line: str, length: int):
    pure_input = input_line.replace('\n', '')
    i = length
    while i < len(pure_input):
        checked = pure_input[i - length:i]
        if len(set(list(pure_input[i - length:i]))) == len(pure_input[i - length:i]):
            break
        i += 1
    return i


class Task06(AdventOfCodeProblem):
    def __init__(self):
        super().__init__()
        self.answer_text = "Start of packet marker after character %d."
        self.bonus_answer_text = "Start of message after character %d."
        self.task_number = 6

    def solve_task(self, input_file_content: List[str]):
        return find_first_occurrence_of_distinct_letters(input_file_content[0], 4)

    def solve_bonus_task(self, input_file_content: List[str]):
        return find_first_occurrence_of_distinct_letters(input_file_content[0], 14)

    def is_input_valid(self, input_file_content: List[str]):
        if len(input_file_content) != 1:
            return False
        pure_line = input_file_content[0].replace('\n', '')
        return pure_line.isalpha() and pure_line.islower()
        # this is based on observation. Checking that it's just one line should also be enough.
