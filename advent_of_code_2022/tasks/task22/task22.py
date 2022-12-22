from advent_of_code_2022.AdventOfCodeTemplate import AdventOfCodeProblem
from typing import List
import re
import numpy as np
from nptyping import NDArray
from itertools import cycle

class Task22(AdventOfCodeProblem):
    board: NDArray
    instructions: List[str]
    turn_list = List[int]
    number_list = List[str]

    def __init__(self, args):
        super().__init__(args)
        self.answer_text = 'The final password is: %d.'
        self.bonus_answer_text = '%d.'
        self.task_number = 22

    def parse_input(self, input_file_content: List[str]):
        board_strings = []
        max_length = 0
        for line in input_file_content:
            if re.fullmatch(' *[.#]+ *\n?', line):
                pure_line = line.replace('\n', '')
                max_length = max(max_length, len(pure_line))
                board_strings.append(pure_line)
            elif re.fullmatch('\n?', line):
                self.board = np.zeros((len(board_strings), max_length))
                for i, line in enumerate(board_strings):
                    for j, str in enumerate(line):
                        if str == '.':
                            self.board[i][j] = 1  # free = 1
                        elif str == '#':
                            self.board[i][j] = 2  # wall = 2
            else:
                self.number_list = [int(x) for x in re.findall('\d+', line)]
                self.turn_list = re.findall('[RL]', line)

    def solve_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        return 0

    def solve_bonus_task(self, input_file_content: List[str]):
        self.parse_input(input_file_content)
        return 0

    def is_input_valid(self, input_file_content: List[str]):
        return all(re.fullmatch('( *[.#]+ *\n?)|(\n?)|([\dRL]+\n?)', line) for line in input_file_content)
