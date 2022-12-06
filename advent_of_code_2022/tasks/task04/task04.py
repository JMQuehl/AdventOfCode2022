import itertools

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


def split_input(line: str) -> List[int]:
    split_parts = line.replace('\n', '').split(',')
    return [int(y) for y in itertools.chain.from_iterable([x.split('-') for x in split_parts])]


class Task04(AdventOfCodeProblem):
    def __init__(self):
        super().__init__()
        self.answer_text = 'One range is fully contained in another %d times.'
        self.bonus_answer_text = 'There are %d overlaps in total.'
        self.task_number = 4

    def solve_task(self, input_file_content: List[str]):
        number_of_includes = 0
        for line in input_file_content:
            split = split_input(line)
            if (split[0] <= split[2] and split[1] >= split[3]) or (split[0] >= split[2] and split[1] <= split[3]):
                number_of_includes += 1
        return number_of_includes

    def solve_bonus_task(self, input_file_content: List[str]):
        number_of_overlaps = 0
        for line in input_file_content:
            split = split_input(line)
            if (split[0] <= split[2] <= split[1]) or (split[2] <= split[0] <= split[3]):
                number_of_overlaps += 1
        return number_of_overlaps

    def is_input_valid(self, input_file_content: List[str]):
        for line in input_file_content:
            pure_line = line.replace('\n', '')
            if not re.fullmatch("[0-9]+-[0-9]+,[0-9]+-[0-9]+", pure_line):
                return False
        return True
