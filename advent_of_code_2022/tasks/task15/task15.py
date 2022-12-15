import re
from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task15(AdventOfCodeProblem):

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "In the row with y=2000000 %d positions cannot contain a beacon."
        self.bonus_answer_text = "%d"
        self.task_number = 15

    def solve_task(self, input_file_content: List[str]):
        return 0

    def solve_bonus_task(self, input_file_content: List[str]):
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("Sensor at x=-?\d+, y=-?\d+: closest beacon is at x=-?\d+, y=-?\d+\n?", line) for line in
            input_file_content)
