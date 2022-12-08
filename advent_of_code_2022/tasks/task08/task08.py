from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import numpy as np


class Task08(AdventOfCodeProblem):
    board: np.array

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'There are %d trees visible.'
        self.bonus_answer_text = 'The highest scenic score is: %d'
        self.task_number = 8

    def parse_input(self, input_file_content: List[str]):
        self.board = np.asarray([list(x.replace('\n', '')) for x in input_file_content]).astype(int)

    def count_trees(self, start_position: (int, int), direction: (int, int)):
        i = start_position[0] + direction[0]
        j = start_position[1] + direction[1]
        counter = 0
        max_height = self.board[start_position]
        while i in range(len(self.board)) and j in range(len(self.board)):
            counter += 1
            if self.board[i, j] >= max_height:
                break
            i += direction[0]
            j += direction[1]
        return counter

    def calc_scenic_score(self, start_position: (int, int)):
        return self.count_trees(start_position, (-1, 0)) * self.count_trees(start_position, (0, -1)) \
               * self.count_trees(start_position, (1, 0)) * self.count_trees(start_position, (0, 1))

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        count = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                if i == 0 or j == 0 or i == len(self.board) - 1 or j == len(self.board[i]) - 1 \
                        or self.board[i][j] > max(self.board[0:i, j]) or self.board[i][j] > max(self.board[i + 1:, j]) \
                        or self.board[i][j] > max(self.board[i, 0:j]) or self.board[i][j] > max(self.board[i, j + 1:]):
                    count += 1
        return count

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        max_score = 0
        for i in range(len(self.board)):
            for j in range(len(self.board[i])):
                score = self.calc_scenic_score((i, j))
                max_score = max(max_score, score)
        return max_score

    def is_input_valid(self, input_file_content: List[str]):
        if len(input_file_content) == 0:
            return False
        row_length = len(input_file_content[0].replace('\n', ''))
        return all(len(elem.replace('\n', '')) == row_length and elem.replace('\n', '').isdigit() for elem in
                   input_file_content)
