from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re


class Task17(AdventOfCodeProblem):
    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'After 2022 rocks have fallen, the tower is %d units tall.'
        self.bonus_answer_text = '%d'
        self.task_number = 17

    def solve_task(self, input_file_content: List[str]):
        return 0

    def solve_bonus_task(self, input_file_content: List[str]):
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return len(input_file_content) == 1 and re.fullmatch("[<>]+\n?", input_file_content[0])
