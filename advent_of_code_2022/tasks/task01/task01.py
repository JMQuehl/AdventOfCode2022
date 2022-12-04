from sortedcontainers import SortedList

from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List


class Task01(AdventOfCodeProblem):
    def __init__(self):
        super().__init__()
        self.answer_text = "The elf carrying the most calories carries food with %d calories."
        self.bonus_answer_text = "The three elves carrying the most calories carry in sum food with %d calories."
        self.task_number = 1

    def solve_task(self, input_file_content: List[str]):
        current_max = 0
        current_calories = 0
        for line in input_file_content:
            if line != '\n':
                current_calories += int(line)
            else:
                current_max = max(current_max, current_calories)
                current_calories = 0

        return max(current_max, current_calories)

    def solve_bonus_task(self, input_file_content: List[str]):
        sorted_calories_list = SortedList()
        current_calories = 0
        for line in input_file_content:
            if line != '\n':
                current_calories += int(line)
            else:
                sorted_calories_list.add(current_calories)
                current_calories = 0
        if current_calories > 0:
            sorted_calories_list.add(current_calories)

        return sorted_calories_list[-1] + sorted_calories_list[-2] + sorted_calories_list[-3]

    def is_input_valid(self, input_file_content: List[str]):
        for line in input_file_content:
            if not line.replace('\n', '').isnumeric() and line != '\n':
                return False
        return True
