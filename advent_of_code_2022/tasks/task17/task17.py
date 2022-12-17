from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
import numpy as np
from nptyping import NDArray


class Task17(AdventOfCodeProblem):
    shapes = [np.array([[0, 0, 1, 1, 1, 1, 0]]),
              np.array([[0, 0, 0, 1, 0, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0],
                        [0, 0, 0, 1, 0, 0, 0]]),
              np.array([[0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 0, 0, 1, 0, 0],
                        [0, 0, 1, 1, 1, 0, 0]]),
              np.array([[0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0],
                        [0, 0, 1, 0, 0, 0, 0]]),
              np.array([[0, 0, 1, 1, 0, 0, 0],
                        [0, 0, 1, 1, 0, 0, 0]])]
    jet_pattern: str
    current_jet = 0
    board: List[NDArray]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'After 2022 rocks have fallen, the tower is %d units tall.'
        self.bonus_answer_text = '%d'
        self.task_number = 17

    def shift_block(self, block: NDArray):
        direction = self.jet_pattern[self.current_jet]
        self.current_jet = (self.current_jet + 1) % len(self.jet_pattern)
        if direction == '<':
            if all(block[:, 0] == 0):
                return np.roll(block, -1)
        else:
            if all(block[:, -1] == 0):
                return np.roll(block, 1)
        return block

    def intersects(self, block: NDArray, line_index: int) -> bool:
        block_section = block[max(0, len(block) - (line_index + 1)):, :]
        board_section = np.array(self.board[-(max(1, 2 + line_index - len(block))):-(2 + line_index):-1])
        return_matrix = block_section + board_section
        return (return_matrix > 1).any()

    def merge_with(self, block: NDArray, line_index: int):
        board_remainder = []
        if line_index >= 0:
            board_slices_to_merge = np.array(self.board[-(max(1, 2 + line_index - len(block))):-(2 + line_index):-1])
            block[(-1 - line_index)::, :] = block[(-1 - line_index)::, :] + board_slices_to_merge
            board_remainder = self.board[len(self.board) - (line_index + 1) + len(block):]
            self.board = self.board[:len(self.board) - (line_index + 1)]
        for x in block[::-1]:
            self.board.append(x)
        self.board.extend(board_remainder)

    def visualize_board(self):
        print('|.......|')
        for line in self.board[::-1]:
            print('|%s|' % ''.join(['.' if x == 0 else '#' for x in line]))
        print('+-------+')
        print('\n')

    def drop_shape(self, identifier: int, height: int = 3):
        block = self.shapes[identifier]
        for i in range(height + 1):
            block = self.shift_block(block)
        max_row = -1
        for row_index in range(len(self.board)):
            if self.intersects(block, row_index):  # collision with something below, break
                max_row = row_index - 1
                break
            else:
                shifted_block = self.shift_block(block)
                if not self.intersects(shifted_block, row_index):
                    block = shifted_block
        self.merge_with(block, max_row)

    def parse_input(self, input_file_content):
        self.jet_pattern = input_file_content[0].replace('\n', '')
        self.board = []

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        for i in range(2022):
            self.drop_shape(i % len(self.shapes), 3)
        return len(self.board)

    def solve_bonus_task(self, input_file_content: List[str]):
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return len(input_file_content) == 1 and re.fullmatch("[<>]+\n?", input_file_content[0])
