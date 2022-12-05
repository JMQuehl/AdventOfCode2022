from abc import ABC, abstractmethod
from typing import List
import os
from advent_of_code_utils import get_input_data, render_markdown_file


class AdventOfCodeProblem(ABC):

    def __init__(self):
        self.answer_text = "The answer to this task is: %s"
        self.bonus_answer_text = "The answer to the bonus task is: %s"
        self.standard_input_file = os.path.join(os.path.dirname(os.path.abspath(__file__)), "input.txt")
        self.task_number = 0

    @abstractmethod
    def solve_task(self, input_file_content: List[str]):
        pass

    @abstractmethod
    def solve_bonus_task(self, input_file_content: List[str]):
        pass

    @abstractmethod
    def is_input_valid(self, input_file_content: List[str]):
        pass

    def print_answer_to_task(self, input_file_content=[], include_bonus_task=True):
        print("Task number %d" % self.task_number)
        if not input_file_content:
            input_file_content = get_input_data(self.task_number)

        if self.is_input_valid(input_file_content):
            print(self.answer_text % self.solve_task(input_file_content))
            if include_bonus_task:
                print(self.bonus_answer_text % self.solve_bonus_task(input_file_content))
        else:
            print("The input is not valid for this task.")

    def render_description(self):
        render_markdown_file(self.task_number)
