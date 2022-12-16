import re
from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple


class Task16(AdventOfCodeProblem):

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = "You can release at most %d pressure."
        self.bonus_answer_text = "%d"
        self.task_number = 16

    def solve_task(self, input_file_content: List[str]):
        return 0

    def solve_bonus_task(self, input_file_content: List[str]):
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return all(
            re.fullmatch("", line) for line in
            input_file_content)
