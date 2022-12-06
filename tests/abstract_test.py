from abc import ABC
from typing import List
from context import advent_of_code_2022
from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem


class TaskTest(ABC):
    task: AdventOfCodeProblem
    known_input: List[str]
    known_output: int
    known_bonus_output: int

    def test_given_example(self):
        assert self.task.solve_task(self.known_input) == self.known_output

    def test_given_bonus_example(self):
        assert self.task.solve_bonus_task(self.known_input) == self.known_bonus_output

    def test_input_validation(self):
        assert self.task.is_input_valid(self.known_input)
