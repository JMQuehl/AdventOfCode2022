from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List, Tuple
import re


class Task20(AdventOfCodeProblem):
    initial_list: List[int]
    mixed_list: List[Tuple[int, int]]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The sum of the three coordinates is: %d.'
        self.bonus_answer_text = 'After using the decryption key and mixing 10 times, the sum of coordinates is: %d.'
        self.task_number = 20

    def parse_input(self, input_file_content: List[str]):
        self.initial_list = []
        for line in input_file_content:
            self.initial_list.append(int(line))

    def initialize_mixed_list(self):
        self.mixed_list = []
        for index, item in enumerate(self.initial_list):
            item = self.initial_list[index]
            self.mixed_list.append((index, item))

    def mix_list(self):
        for i in range(len(self.initial_list)):
            value = self.initial_list[i]
            index_in_mixed_list = [x for x, tup in enumerate(self.mixed_list) if tup[0] == i][0]
            tup = self.mixed_list.pop(index_in_mixed_list)
            self.mixed_list.insert((index_in_mixed_list + value) % len(self.mixed_list), tup)

    def calculate_coordinates(self) -> int:
        zero_idx_in_mixed_list = [x for x, tup in enumerate(self.mixed_list) if tup[1] == 0][0]
        return self.mixed_list[(1000 + zero_idx_in_mixed_list) % len(self.mixed_list)][1] + \
            self.mixed_list[(2000 + zero_idx_in_mixed_list) % len(self.mixed_list)][1] + \
            self.mixed_list[(3000 + zero_idx_in_mixed_list) % len(self.mixed_list)][1]

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.initialize_mixed_list()
        self.mix_list()
        return self.calculate_coordinates()

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        self.initial_list = [x * 811589153 for x in self.initial_list]
        self.initialize_mixed_list()
        for i in range(10):
            self.mix_list()
        return self.calculate_coordinates()

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch("-?\d+\n?", line) for line in input_file_content)
